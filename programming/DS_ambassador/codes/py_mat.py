import numpy as np
import matplotlib.pyplot as plt

# To make text looks better
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)


# create data points
x = np.arange(0, 10, 0.1)         # from 0 to 10 with step 0.1
x = np.linspace(0, 2*np.pi, 100)  # 100 points from 0 to 2pi
y_sin = np.sin(x)
y_cos = np.cos(x)


# plot the data
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.xlim(0, 2*np.pi)                     # set x limits
plt.ylim(-1.5, 1.5)                      # set y limits
plt.yscale('linear')                     # set y scale to linear
plt.xlabel(r'time $\tau$', fontsize=12)  # set x label
plt.ylabel('trigonometric')              # set y label
plt.xticks(fontsize=18)                  # set x ticks font size
plt.yticks(fontsize=18)                  # set y ticks font size
plt.title('Math sine/cosine function', loc="right", fontsize=20)
plt.legend(loc='upper right')
plt.tight_layout()  # remove the white space around the plot
plt.show()

# save the plot
# plt.savefig('plot.png', dpi=300, bbox_inches='tight')



# histogram
data = np.random.randn(1000)  # 1000 random numbers from a normal distribution
plt.hist(data, bins=20, density=True, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
plt.show()


# scatter
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y, marker='o', color='steelblue', edgecolor='none', alpha=0.5)
plt.show()


# bar
x = np.arange(5)
y = np.random.randint(1, 10, 5)
plt.bar(x, y, color='steelblue', edgecolor='none', alpha=0.5)
plt.show()
