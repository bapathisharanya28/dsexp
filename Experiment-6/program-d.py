import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(100),
index=pd.date_range('2024-01-01', periods=100))
ts_monthly = ts.resample('M').mean()
print(ts_monthly)