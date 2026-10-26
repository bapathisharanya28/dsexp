import matplotlib.pyplot as plt
x=[13,20,23,27,30]
y=[15,20,25,30,35]
plt.plot(x,y)
plt.title('line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.savefig('line-plot.png')
plt.show()