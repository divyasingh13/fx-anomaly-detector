import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats

ticker = yf.download("EURUSD=X", period="3mo", interval="1d")

close_prices = ticker["Close"]["EURUSD=X"]
daily_changes = close_prices.diff()

mean = daily_changes.mean()
std = daily_changes.std()
anomalies = daily_changes[abs(daily_changes) > 2 * std]

print("Mean daily change:", round(mean, 6))
print("Standard deviation:", round(std, 6))
print("\nAnomalies detected:")
print(anomalies)

plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True)
fig.suptitle('EUR/USD FX Rate — Anomaly Detection (Last 3 Months)',
             fontsize=16, fontweight='bold', color='white', y=0.98)

ax1.plot(close_prices.index, close_prices.values,
         color='#00BFFF', linewidth=1.5, label='EUR/USD Close Price')

rolling_mean = close_prices.rolling(5).mean()
rolling_std = close_prices.rolling(5).std()
ax1.fill_between(close_prices.index,
                 rolling_mean - 2 * rolling_std,
                 rolling_mean + 2 * rolling_std,
                 alpha=0.15, color='#00BFFF', label='Normal Range (2σ)')

ax1.scatter(anomalies.index, close_prices[anomalies.index],
            color='red', s=120, zorder=5, label='Anomaly Detected')

for date, value in close_prices[anomalies.index].items():
    ax1.annotate(date.strftime('%b %d'),
                 xy=(date, value),
                 xytext=(10, 10),
                 textcoords='offset points',
                 color='red', fontsize=9,
                 arrowprops=dict(arrowstyle='->', color='red', lw=1))

ax1.set_ylabel('Exchange Rate', color='white')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.2)
ax1.tick_params(colors='white')

colors = ['red' if abs(v) > 2 * std else '#00BFFF'
          for v in daily_changes.fillna(0)]
ax2.bar(daily_changes.index, daily_changes.values, color=colors, width=0.8)
ax2.axhline(y=2 * std, color='yellow', linestyle='--',
            linewidth=1, alpha=0.7, label='+2σ threshold')
ax2.axhline(y=-2 * std, color='yellow', linestyle='--',
            linewidth=1, alpha=0.7, label='-2σ threshold')
ax2.set_ylabel('Daily Change', color='white')
ax2.set_xlabel('Date', color='white')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.2)
ax2.tick_params(colors='white')

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax2.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
plt.xticks(rotation=45, color='white')

plt.tight_layout()
plt.savefig('fx_anomaly_chart.png', dpi=150,
            bbox_inches='tight', facecolor='#1a1a2e')
print("Chart saved as fx_anomaly_chart.png")
