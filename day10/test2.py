import numpy as np

M = np.array([[1, 0], [0, 1]])
N = np.array([[3, 2, 1], [0, 1, 2]])

X = np.array([[1],[2],[3]])

#for i in range(n):
#    for j in range(n):
#        for k in range(n):
#            print(i.j.k)
def set_values(n, threshold, values_list=[]):
    print(threshold)
    if len(values_list) >= threshold:
        yield values_list
    for i in range(n):
        values_list.append(i)
        yield from set_values(n, threshold, values_list)
        values_list = []

       # for j in range(n):
       #     for k in range(n):
       #         values_list = [i,j,k]
       #         yield values_list

lst = set_values(3, 3)
print(lst)
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))





    
