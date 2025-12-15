import math
class Box:
    def __init__(self, position):
        self.position = position
        self.group = None
        self.min_distance = 0

def get_distance(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2+(x[2]-y[2])**2

def get_nearest(data, e):
    min_d = float("inf")
    nearest = None
    for point in data:
        if point == e:
            continue
        d = ((e.position[0] - point.position[0])**2 +
                (e.position[1] - point.position[1])**2 + 
                (e.position[2] - point.position[2])**2
                )
        if d < min_d:
            nearest = point
            min_d = d
    return nearest, min_d

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
counter = 1
groups = {}
groups[counter] = set() 
for a, b in sorted_pairs[:1000]:
    if a.group is None and b.group is None:
        a.group = counter
        b.group = counter
        groups[counter].add(a)
        groups[counter].add(b)
        counter += 1
        groups[counter] = set() 
        continue
    if a.group is None:
        a.group = b.group
        groups[b.group].add(a)
        continue
    if b.group is None:
        b.group = a.group
        groups[a.group].add(b)
        continue
    if a.group != b.group:
        old = a.group
        new = b.group
        for elm in groups[old]:
            groups[new].add(elm)
            elm.group = new
        del groups[old]
counter_d = {}
for k,v in groups.items():
    counter_d[k] = len(v)
lst = sorted(counter_d.values(), reverse=True)
print(lst[0]*lst[1]*lst[2])
