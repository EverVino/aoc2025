import math
class Box:
    def __init__(self, position):
        self.position = position
        self.group = None
        self.min_distance = 0

def get_distance(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2+(x[2]-y[2])**2

def open_data(path="input.txt"):
    with open(path, "r") as f:
        reader = f.read().splitlines()
    data = []
    for line in reader:
        x,y,z = line.split(",")
        e = Box((int(x),int(y),int(z)))
        data.append(e)

    pairs = []
    distances = []
    n = len(data)
    for i in range(n):
        for j in range(i+1,n):
            pairs.append((data[i],data[j]))
            distances.append(get_distance(data[i].position,data[j].position)) 

    return data, pairs, distances 

data, pairs, distances = open_data()
sorted_pairs = [x for _, x in sorted(zip(distances,pairs))] 
seen = set()
n = len(data)
for a,b in sorted_pairs:
    if a not in seen:
        seen.add(a)
    if b not in seen:
        seen.add(b)
    if len(seen) == n:
        print(a.position, b.position)
        print(a.position[0]*b.position[0])
        break

