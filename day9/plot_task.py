import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def open_data(path="input.txt"):
    with open(path, "r") as f:
        reader = f.read().splitlines()

    data = []
    for line in reader:
        x,y = line.split(",")
        try:
            data.append((int(x),int(y)))
        except Exception as e:
            print(e)
            print(line)
            print(x,y)

    return data


data = open_data()
n = 0
m = 0
for p in data:
    x, y = p
    if x> n:
        n = x
    if y> m:
        m = y

matrix = np.zeros((n+2,m+2), dtype=np.bool_)

for p in data:
    x,y =p
    matrix[x,y] = 1

plt.matshow(matrix)
plt.colorbar()
plt.show()
