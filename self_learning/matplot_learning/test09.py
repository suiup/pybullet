import matplotlib.pyplot as plt

plt.plot(range(5), range(5), linestyle='--', drawstyle='steps')
plt.plot(range(5), range(5)[::-1], linestyle=':', drawstyle='steps')
plt.xlim([-1, 5])
plt.ylim([-1, 5])
plt.show()