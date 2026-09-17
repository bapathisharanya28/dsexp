import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'Category':['A','B','C'],'values':[12,24,55]})
df.plot(kind='bar',x='Category',y='values')
plt.title('Bar Plot')
plt.show()