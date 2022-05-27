import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg') #For macOS

D = np.loadtxt("xi1.d")
X = D[:4096, 0] * 800.0 / np.pi
XI1_a = D[4096 * 10:4096 * 11, 1]
XI1_b = D[4096 * 30:4096 * 31, 1]

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.serif": ["Helvetica"]})

plt.plot(X, XI1_a, linestyle = 'dashed', label = r"$(M_1,M_2,t)=(1,1,10)$")
plt.plot(X, XI1_b, label = r"$(M_1,M_2,t)=(1,1,30)$")

plt.xlim(-0.2 * 800 / np.pi, 0.2 * 800 / np.pi)
plt.xlabel(r"$x$", fontsize = 15)
plt.ylabel(r"$\xi_1(x,t)$", fontsize = 15)
plt.legend(loc = 2)
plt.grid()
plt.tight_layout()
plt.show()
plt.clf()

