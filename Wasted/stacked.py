import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Convert dates to datetime if not already
df_actions_a2c.index = pd.to_datetime(df_actions_a2c.index)
df_actions_ppo.index = pd.to_datetime(df_actions_ppo.index)
"""df_actions_ddpg.index = pd.to_datetime(df_actions_ddpg.index)
df_actions_td3.index = pd.to_datetime(df_actions_td3.index)"""
df_actions_sac.index = pd.to_datetime(df_actions_sac.index)

# Set up the figure
fig, axes = plt.subplots(3, 1, figsize=(14, 16))
fig.suptitle('Portfolio Weight Evolution (100% Stacked)', fontsize=16)

# Define groups - separate stocks and crypto for coloring
crypto_tickers = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'USDT-USD', 'BNB-USD', 'DOGE-USD', 
                 'ADA-USD', 'TRX-USD', 'XLM-USD']
stock_tickers = [col for col in df_actions_a2c.columns if col not in crypto_tickers]

# Color schemes
crypto_colors = plt.cm.Reds(np.linspace(0.3, 0.8, len(crypto_tickers)))
stock_colors = plt.cm.Blues(np.linspace(0.3, 0.8, len(stock_tickers)))

# Create a dictionary mapping tickers to colors
colors_dict = {}
for i, ticker in enumerate(crypto_tickers):
    colors_dict[ticker] = crypto_colors[i]
for i, ticker in enumerate(stock_tickers):
    colors_dict[ticker] = stock_colors[i]

# A2C portfolio weights stacked area plot
axes[0].stackplot(df_actions_a2c.index, 
                 [df_actions_a2c[ticker] for ticker in df_actions_a2c.columns],
                 labels=df_actions_a2c.columns,
                 colors=[colors_dict[ticker] for ticker in df_actions_a2c.columns],
                 alpha=0.8)
axes[0].set_title('A2C Portfolio Allocation Over Time', fontsize=14)
axes[0].set_xlabel('Date', fontsize=12)
axes[0].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes[0].set_ylim(0, 1)
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes[0].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes[0].grid(True, linestyle='--', alpha=0.3)

# PPO portfolio weights stacked area plot
axes[1].stackplot(df_actions_ppo.index, 
                 [df_actions_ppo[ticker] for ticker in df_actions_ppo.columns],
                 labels=df_actions_ppo.columns,
                 colors=[colors_dict[ticker] for ticker in df_actions_ppo.columns],
                 alpha=0.8)
axes[1].set_title('PPO Portfolio Allocation Over Time', fontsize=14)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes[1].set_ylim(0, 1)
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes[1].grid(True, linestyle='--', alpha=0.3)
"""
# DDPG portfolio weights stacked area plot
axes[2].stackplot(df_actions_ddpg.index,
                    [df_actions_ddpg[ticker] for ticker in df_actions_ddpg.columns],
                    labels=df_actions_ddpg.columns,
                    colors=[colors_dict[ticker] for ticker in df_actions_ddpg.columns],
                    alpha=0.8)
axes[2].set_title('DDPG Portfolio Allocation Over Time', fontsize=14)
axes[2].set_xlabel('Date', fontsize=12)
axes[2].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes[2].set_ylim(0, 1)
axes[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes[2].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes[2].grid(True, linestyle='--', alpha=0.3)

# TD3 portfolio weights stacked area plot
axes[3].stackplot(df_actions_td3.index,
                    [df_actions_td3[ticker] for ticker in df_actions_td3.columns],
                    labels=df_actions_td3.columns,
                    colors=[colors_dict[ticker] for ticker in df_actions_td3.columns],
                    alpha=0.8)
axes[3].set_title('TD3 Portfolio Allocation Over Time', fontsize=14)
axes[3].set_xlabel('Date', fontsize=12)
axes[3].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes[3].set_ylim(0, 1)
axes[3].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes[3].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes[3].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes[3].grid(True, linestyle='--', alpha=0.3)
"""
# SAC portfolio weights stacked area plot
axes[2].stackplot(df_actions_sac.index,
                    [df_actions_sac[ticker] for ticker in df_actions_sac.columns],
                    labels=df_actions_sac.columns,
                    colors=[colors_dict[ticker] for ticker in df_actions_sac.columns],
                    alpha=0.8)
axes[2].set_title('SAC Portfolio Allocation Over Time', fontsize=14)
axes[2].set_xlabel('Date', fontsize=12)
axes[2].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes[2].set_ylim(0, 1)
axes[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes[2].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes[2].grid(True, linestyle='--', alpha=0.3)


# Create separate legend figures for crypto and stocks
# This makes the legend more readable
fig_legend = plt.figure(figsize=(14, 4))
gs = fig_legend.add_gridspec(2, 1)

# Crypto legend
ax1 = fig_legend.add_subplot(gs[0])
for i, ticker in enumerate(crypto_tickers):
    ax1.plot([], [], color=colors_dict[ticker], label=ticker, linewidth=6)
ax1.axis('off')
ax1.legend(loc='center', ncol=5, title='Cryptocurrencies', fontsize=10)

# Stock legend
ax2 = fig_legend.add_subplot(gs[1])
for i, ticker in enumerate(stock_tickers):
    ax2.plot([], [], color=colors_dict[ticker], label=ticker, linewidth=6)
ax2.axis('off')
ax2.legend(loc='center', ncol=10, title='Stocks', fontsize=10)

# Add summary text with allocation percentages
# Calculate average allocations
a2c_crypto_alloc = df_actions_a2c[crypto_tickers].sum(axis=1).mean()
a2c_stock_alloc = df_actions_a2c[stock_tickers].sum(axis=1).mean()
ppo_crypto_alloc = df_actions_ppo[crypto_tickers].sum(axis=1).mean()
ppo_stock_alloc = df_actions_ppo[stock_tickers].sum(axis=1).mean()

fig.text(0.5, 0.01, 
        f"Average Allocations:\nA2C: Crypto {a2c_crypto_alloc:.2%}, Stocks {a2c_stock_alloc:.2%}\nPPO: Crypto {ppo_crypto_alloc:.2%}, Stocks {ppo_stock_alloc:.2%}",
        ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.subplots_adjust(hspace=0.3, bottom=0.08)

# Show the plot
plt.show()

# Create simplified version showing only major asset classes
fig2, axes2 = plt.subplots(3, 1, figsize=(14, 10))
fig2.suptitle('Asset Class Allocation Over Time', fontsize=16)

# A2C - Group by asset class
a2c_crypto = df_actions_a2c[crypto_tickers].sum(axis=1)
a2c_stocks = df_actions_a2c[stock_tickers].sum(axis=1)

# PPO - Group by asset class
ppo_crypto = df_actions_ppo[crypto_tickers].sum(axis=1)
ppo_stocks = df_actions_ppo[stock_tickers].sum(axis=1)
"""
# DDPG - Group by asset class
ddpg_crypto = df_actions_ddpg[crypto_tickers].sum(axis=1)
ddpg_stocks = df_actions_ddpg[stock_tickers].sum(axis=1)

# TD3 - Group by asset class
td3_crypto = df_actions_td3[crypto_tickers].sum(axis=1)
td3_stocks = df_actions_td3[stock_tickers].sum(axis=1)
"""
# SAC - Group by asset class
sac_crypto = df_actions_sac[crypto_tickers].sum(axis=1)
sac_stocks = df_actions_sac[stock_tickers].sum(axis=1)

# A2C asset class stacked plot
axes2[0].stackplot(df_actions_a2c.index, 
                  [a2c_crypto, a2c_stocks],
                  labels=['Cryptocurrencies', 'Stocks'],
                  colors=['#e63946', '#457b9d'],
                  alpha=0.8)
axes2[0].set_title('A2C Asset Class Allocation', fontsize=14)
axes2[0].set_xlabel('Date', fontsize=12)
axes2[0].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes2[0].set_ylim(0, 1)
axes2[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes2[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes2[0].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes2[0].grid(True, linestyle='--', alpha=0.3)
axes2[0].legend(loc='upper right')

# PPO asset class stacked plot
axes2[1].stackplot(df_actions_ppo.index, 
                  [ppo_crypto, ppo_stocks],
                  labels=['Cryptocurrencies', 'Stocks'],
                  colors=['#e63946', '#457b9d'], 
                  alpha=0.8)
axes2[1].set_title('PPO Asset Class Allocation', fontsize=14)
axes2[1].set_xlabel('Date', fontsize=12)
axes2[1].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes2[1].set_ylim(0, 1)
axes2[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes2[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes2[1].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes2[1].grid(True, linestyle='--', alpha=0.3)
axes2[1].legend(loc='upper right')
"""
# DDPG asset class stacked plot
axes2[2].stackplot(df_actions_ddpg.index, 
                  [ddpg_crypto, ddpg_stocks],
                  labels=['Cryptocurrencies', 'Stocks'],
                  colors=['#e63946', '#457b9d'], 
                  alpha=0.8)
axes2[2].set_title('DDPG Asset Class Allocation', fontsize=14)
axes2[2].set_xlabel('Date', fontsize=12)
axes2[2].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes2[2].set_ylim(0, 1)
axes2[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes2[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes2[2].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes2[2].grid(True, linestyle='--', alpha=0.3)
axes2[2].legend(loc='upper right')

# TD3 asset class stacked plot
axes2[3].stackplot(df_actions_td3.index, 
                  [td3_crypto, td3_stocks],
                  labels=['Cryptocurrencies', 'Stocks'],
                  colors=['#e63946', '#457b9d'], 
                  alpha=0.8)
axes2[3].set_title('TD3 Asset Class Allocation', fontsize=14)
axes2[3].set_xlabel('Date', fontsize=12)
axes2[3].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes2[3].set_ylim(0, 1)
axes2[3].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes2[3].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes2[3].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes2[3].grid(True, linestyle='--', alpha=0.3)
axes2[3].legend(loc='upper right')
"""
# SAC asset class stacked plot
axes2[2].stackplot(df_actions_sac.index, 
                  [sac_crypto, sac_stocks],
                  labels=['Cryptocurrencies', 'Stocks'],
                  colors=['#e63946', '#457b9d'], 
                  alpha=0.8)
axes2[2].set_title('SAC Asset Class Allocation', fontsize=14)
axes2[2].set_xlabel('Date', fontsize=12)
axes2[2].set_ylabel('Portfolio Weight (%)', fontsize=12)
axes2[2].set_ylim(0, 1)
axes2[2].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.0%}'.format(x)))
axes2[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
axes2[2].xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes2[2].grid(True, linestyle='--', alpha=0.3)
axes2[2].legend(loc='upper right')

plt.tight_layout()
plt.show()
