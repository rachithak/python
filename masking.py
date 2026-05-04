import numpy as np
a = np.array([230, 10, 284, 39, 76])
cutoff = 200
a[a > cutoff] = 0
print(a)