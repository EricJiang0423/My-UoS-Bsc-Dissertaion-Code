    def garch_evt_cvar_new(self, returns, confidence_level=None, threshold_quantile=None):
        """Compute Conditional Value at Risk (CVaR) using GARCH-EVT model.
        
        This method combines GARCH for volatility clustering and EVT (Extreme Value Theory)
        to model tail risk using the Generalized Pareto Distribution (GPD).
        
        Parameters:
            returns: numpy.ndarray - Historical return series
            confidence_level: float - Confidence level, defaults to self.confidence_level
            threshold_quantile: float - Quantile for EVT threshold, defaults to self.threshold_quantile
            
        Returns:
            tuple: (VaR, CVaR) - Value at Risk and Conditional Value at Risk
        """
        if confidence_level is None:
            confidence_level = self.confidence_level
        if threshold_quantile is None:
            threshold_quantile = self.threshold_quantile
        
        if len(returns) < 30:
            return 0, -0.1  # Conservative estimate for insufficient data
        
        try:
            # Step 1: Fit GARCH(1,1) model to get standardized residuals
            scaling_const = 10.0 / (returns.std() if returns.std() > 0 else 1.0)
            scaled_returns = scaling_const * returns
        
            model = arch_model(scaled_returns, mean='constant', vol='GARCH', p=1, q=1, dist='skewstudent')
            res = model.fit(disp='off', show_warning=False)
            
            std_residuals = res.resid / res.conditional_volatility
        
            # Step 2: EVT Analysis (GPD Fitting)
            threshold = np.percentile(std_residuals, threshold_quantile * 100)
            exceedances = std_residuals[std_residuals < threshold] - threshold
        
            if len(exceedances) < 10:
                var_empirical = -np.quantile(returns, 1 - confidence_level)
                cvar_empirical = -np.mean(returns[returns <= -var_empirical])
                return var_empirical, cvar_empirical
        
            # MLE estimation for GPD parameters
            def gpd_neg_log_likelihood(params, data):
                xi, beta = params
                if beta <= 0 or xi < -1 or xi > 1:
                    return np.inf
                likelihoods = (1 + xi * (data - min(data)) / beta) ** (-1 / xi)
                return -np.sum(np.log(likelihoods))
            
            initial_params = [0.1, 1]
            bounds = [(-1, 1), (1e-5, None)]
            gpd_fit = minimize(gpd_neg_log_likelihood, initial_params, args=(exceedances,), method='L-BFGS-B', bounds=bounds)
            xi_hat, beta_hat = gpd_fit.x
            xi_hat = min(xi_hat, 0.99)
        
            N = len(std_residuals)
            Nu = len(exceedances)
            q = 1 - confidence_level
        
            if xi_hat != 0:
                var_evt = threshold + (beta_hat / xi_hat) * (((N / Nu) * q) ** (-xi_hat) - 1)
                cvar_evt = (var_evt + (beta_hat - xi_hat * threshold) / (1 - xi_hat))
            else:
                var_evt = threshold + beta_hat * np.log(N / Nu * q)
                cvar_evt = var_evt + beta_hat
        
            # Step 3: Adjust for GARCH Conditional Volatility
            forecasts = res.forecast(horizon=1)
            cond_vol = float(forecasts.variance.iloc[-1]) ** 0.5 / scaling_const
        
            var_adjusted = var_evt * cond_vol
            cvar_adjusted = cvar_evt * cond_vol
        
            return var_adjusted, cvar_adjusted
        
        except Exception:
            # Fallback: Historical simulation if GARCH-EVT fails
            try:
                var_hist = -np.quantile(returns, 1 - confidence_level)
                cvar_hist = -np.mean(returns[returns <= -var_hist])
                return var_hist, cvar_hist
            except:
                return 0, 0.1