import pandas as pd
p = pd.Period('2024Q1')
print(p + 1)
print(p.asfreq('M', 'end'))