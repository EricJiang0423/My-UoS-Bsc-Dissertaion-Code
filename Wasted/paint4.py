from config_tickers import DOW_30_TICKER, CRYPTO_TICKER

# 计算每个股票的归一化价格（以1美元为基准）
df['normalized_close'] = df.groupby('tic')['close'].transform(lambda x: x / x.iloc[0])

# 绘制DOW_30_TICKER股票走势
plt.figure(figsize=(14, 10))
for tic in DOW_30_TICKER:
    if tic in df['tic'].unique():
        plt.plot(df[df['tic'] == tic]['date'], df[df['tic'] == tic]['normalized_close'], label=tic)

plt.xlabel('Date')
plt.ylabel('Normalized Close Price (Starting from $1)')
plt.title('Normalized Stock Prices for DOW 30 (Starting from $1)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gcf().autofmt_xdate()
# 使用对数Y轴
plt.yscale('log')

# 添加网格线 - 主刻度和次刻度
plt.grid(True, which='major', axis='y', linestyle='-', alpha=0.7)
plt.grid(True, which='minor', axis='y', linestyle='--', alpha=0.4)
#添加水平参考线，比如初始价格(1.0)
plt.axhline(y=1.0, color='k', linestyle='-', alpha=0.3)
plt.text(df['date'].min(), 1.02, 'Initial Price', 
         verticalalignment='bottom', horizontalalignment='left', fontsize=10)

plt.tight_layout()
plt.show()

# 绘制CRYPTO_TICKER股票走势
plt.figure(figsize=(14, 10))
for tic in CRYPTO_TICKER:
    if tic in df['tic'].unique():
        plt.plot(df[df['tic'] == tic]['date'], df[df['tic'] == tic]['normalized_close'], label=tic)

plt.xlabel('Date')
plt.ylabel('Normalized Close Price (Starting from $1)')
plt.title('Normalized Cryptocurrency Prices (Starting from $1)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()

# 使用对数Y轴
plt.yscale('log')

# 添加网格线 - 主刻度和次刻度
plt.grid(True, which='major', axis='y', linestyle='-', alpha=0.7)
plt.grid(True, which='minor', axis='y', linestyle='--', alpha=0.4)
#添加水平参考线，比如初始价格(1.0)
plt.axhline(y=1.0, color='k', linestyle='-', alpha=0.3)
plt.text(df['date'].min(), 1.02, 'Initial Price', 
         verticalalignment='bottom', horizontalalignment='left', fontsize=10)

plt.show()
# 计算每个资产的每日增长率
df['daily_return'] = df.groupby('tic')['close'].pct_change()

# 绘制DOW_30_TICKER资产的增长率走势图
plt.figure(figsize=(14, 10))
for tic in DOW_30_TICKER:
    if tic in df['tic'].unique():
        plt.plot(df[df['tic'] == tic]['date'], df[df['tic'] == tic]['daily_return'], label=tic)

plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title('Daily Return for DOW 30')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gcf().autofmt_xdate()
plt.yscale('linear')
plt.show()

# 绘制CRYPTO_TICKER资产的增长率走势图
plt.figure(figsize=(14, 10))
for tic in CRYPTO_TICKER:
    if tic in df['tic'].unique():
        plt.plot(df[df['tic'] == tic]['date'], df[df['tic'] == tic]['daily_return'], label=tic)

plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title('Daily Return for Cryptocurrencies')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gcf().autofmt_xdate()
plt.yscale('linear')
plt.show()
