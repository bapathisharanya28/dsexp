import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(500)
sns.histplot(data,kde=True)
plt.title('Histogram and density')
plt.show()