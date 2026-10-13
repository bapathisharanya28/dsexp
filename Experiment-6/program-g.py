import pandas as pd
dates = pd.date_range("2026-01-01 00:00", periods=12, freq="h")
values = [10, 12, 15, 14, 18, 20, 22, 21, 25, 28, 30, 32]
ts = pd.Series(values, index=dates)
print("Original hourly time series:")
print(ts)
print("\nResampling - 3-hour mean:")
print(ts.resample("3h").mean())
print("\nDownsampling - 4-hour sum:")
print(ts.resample("4h").sum())
print("\nUpsampling - 30-minute intervals:")
print(ts.resample("30min").asfreq())
print("\nUpsampling with forward fill:")
print(ts.resample("30min").ffill())
