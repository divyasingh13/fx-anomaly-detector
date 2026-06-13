# FX Anomaly Detector

A Python tool that detects statistically unusual movements in FX exchange rates using the 2-sigma rule.

## What it does
- Downloads live EUR/USD exchange rate data from Yahoo Finance
- Calculates daily price changes
- Flags any day where the movement exceeds 2 standard deviations from the mean
- Visualizes normal vs anomalous movements on a dual-panel chart

## Why I built this
I spent 3 years at Morgan Stanley working on FX trade operations — validating pricing flows, tracing trades from execution to settlement, and ensuring regulatory reporting accuracy. Anomaly detection is a core part of that work. This project combines that domain knowledge with Python data analysis.

## What it found
Running this tool on the last 3 months of EUR/USD data automatically detected the April 2026 tariff-driven FX volatility — 4 anomalous days where the rate moved more than 2 standard deviations from normal.

## Tech used
- Python 3.12
- yfinance — live FX data
- pandas — data manipulation
- matplotlib — visualization
- scipy — statistical analysis

## How to run it
pip install pandas yfinance matplotlib scipy

python fx_anomaly.py

## Output
The tool generates fx_anomaly_chart.png showing:
- Top panel: EUR/USD price with shaded normal range and anomaly markers
- Bottom panel: Daily changes with 2σ threshold lines highlighted
