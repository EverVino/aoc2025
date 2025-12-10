class Box:
    def __init__(self, position):
        self.position = position
        self.group = None
        self.min_distance = 0

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

def open_data(path="test.txt"):
    with open(path, "r") as f:
        reader = f.read().splitlines()

    data = []
    for line in reader:
        x,y,z = line.split(",")
        e = Box((int(x),int(y),int(z)))
        data.append(e)

    seen = set()
    nearest_pairs = [] 
    for e in data:
        if e in seen:
            continue
        f, distance = get_nearest(data, e)
        e.min_distance = distance
        seen.add(f)
        nearest_pairs.append((e,f))

    return data, nearest_pairs

data, nearest_pairs = open_data()

for m, n in nearest_pairs:
    print(m.position,n.position,m.min_distance)
