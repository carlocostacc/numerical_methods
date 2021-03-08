from backwarderror import *
from forwarderror import *
from regression import *
import numpy as np

a = np.array([[3,2],[-1,2]])
ans = np.array([[18],[2]])
Xr = np.array([[3],[5]])

# backward_error(a, ans, Xr, 2, 2)
# forward_error(a, ans, Xr, 2, 2)
# linear_regression([1, 2, 3, 4, 5, 6, 7], [0.5, 2.5, 2, 4, 3.5, 6, 5.5], 0.071428, 0.839285)
# errorminimization([1, 2, 3, 4, 5, 6, 7], [0.5, 2.5, 2, 4, 3.5, 6, 5.5])
# exponential_regression([1,2,4,8,12,15,19,23,27,29,30,32,33], [2250, 2500, 5000, 29000, 120000, 275000, 1180000, 3100000,\
#                                                               7500000, 24000000, 42000000, 220000000, 410000000])
power_regression([0.912, 0.986,1.06, 1.13, 1.19, 1.26, 1.32, 1.38, 1.41, 1.49], [13.7, 15.9, 18.5, 21.3, 23.5, 27.2,
                                                                                32.7, 36, 38.6, 43.7])