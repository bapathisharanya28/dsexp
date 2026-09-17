import pandas as pd
ts = pd.Timestamp.now()
ts_utc = ts.tz_localize('UTC')
ts_ind = ts_utc.tz_convert('Asia/Kolkata')
print(ts_ind)