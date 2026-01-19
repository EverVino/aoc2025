
import numpy as np

A = np.array([[1.59872115546023e-14],
 [12.0000000000000],
 [5.99999999999998],
 [6.00000000000001],
 [10.0000000000000],
 [1.77635683940025e-14],
 [14.0000000000000],
 [4.99999999999995],
 [5.00000000000001],
 [16.0000000000000]])
print(A)
print(np.round(A, decimals=2).astype(int))
print((np.round(A, decimals=2).astype(int)!=A.astype('int')).any())
rA=np.round(A, decimals=2).astype(int)
valid = (rA -A).sum() < 1e-5
print(valid)


