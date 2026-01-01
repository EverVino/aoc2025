
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
def get_dim(data):
    my = 0
    mx = 0
    for point in data:
        x,y = point
        if x>mx:
            mx=x
        if y>my:
            my=y
    return my+2, mx+2

def get_borders(data):
    n = len(data)
    pairs = {}
    for i in range(n):
        for j in range(n):
            if data[i]==data[j]:
                continue
            x1, y1 = data[i]
            x2, y2 = data[j]
            if x1 == x2:
                if (x1,y1) not in pairs:
                    pairs[(x1,y1)] = []
                pairs[(x1,y1)].append((x2,y2))
            if y1 == y2:
                if (x1,y1) not in pairs:
                    pairs[(x1,y1)] = []
                pairs[(x1,y1)].append((x2,y2))

    for k, v in pairs.items():
        if len(v) > 2:
            print(k, v)
            x, y=k 
            for p in v:
                xi,yi = p
                if yi!=y:
                    print(p, pairs[p])
                
        if len(v)<2:
            print(k,v)

data = open_data()
rows, cols = get_dim(data)
#matrix = [[0 for _ in range(cols)] for __ in range(rows)]
#for point in data:
#    x, y = point
#    matrix[y][x] = 1

get_borders(data)
