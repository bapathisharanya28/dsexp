import pandas as pd
import numpy as np
rng = pd.date_range('2023-01-01', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)