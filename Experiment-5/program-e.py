import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.boxplot(data=np.random.randn(80,4))
plt.title('box plot')
plt.show()