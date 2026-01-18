
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
            x, y=k 
            nl = []
            ol = []
            for p in v:
                xi, yi = p
                if yi != y:
                    nl.append(p)
                else:
                    ol.append(p)
            nol = sorted(ol, key= lambda m:abs(m[0]-x))
            nl.append(nol[0])
            pairs[k] = nl
        
        if len(v)<2:
            print(k,v)
    return pairs

data = open_data()
#rows, cols = get_dim(data)
#matrix = [[0 for _ in range(cols)] for __ in range(rows)]
#for point in data:
#    x, y = point
#    matrix[y][x] = 1

pairs = get_borders(data)
borders = [] 
for k, v in pairs.items():
    for p in v:
        border = sorted((k,p))
        if border not in borders:
            borders.append(border)
print(len(borders))
print(len(pairs))

def get_vs(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1>x2:
        xM = x1
        xm = x2
    else:
        xM = x2
        xm = x1
    if y1>y2:
        yM = y1
        ym = y2
    else:
        yM = y2
        ym = y1
    return xm, xM, ym, yM

def intersection(xm, xM, ym, yM, borders):
    for border in borders:
        p1, p2 = border
        x1, y1 = p1
        x2, y2 = p2
        ys = sorted((y1,y2))
        xs = sorted((x1,x2))
        c = 0
        # check if border is vertical
        if x1 == x2:
            if xm<x1<xM:
                if ys[0]<ym<ys[1]:
                    c += 1
                if ys[0]<yM<ys[1]:
                    c += 1
        if y1==y2:
            if ym<y1<yM:
                if xs[0]<xm<xs[1]:
                    c += 1
                if xs[0]<xM<xs[1]:
                    c += 1
    return not c%2==0 

n = len(data)
A = 0
for i in range(n):
    for j in range(i+1,n):
        p1 = data[i]
        p2 = data[j]
    xm, xM, ym, yM = get_vs(p1,p2)
    if not intersection(xm, xM, ym, yM, borders):
        a = (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)
        print(a)
        if abs(a) > A:
            A = abs(a)

print(A)
# check borders
#n = len(borders)
#counter = {}
#for k in pairs.keys():
#    for j in range(n):
#        p1, p2 = borders[j]
#        if p1 == k or p2 == k:
#            if k not in counter:
#                counter[k] = 0
#            counter[k] += 1
#
#start = borders[0][0]
#init_ = borders[0][0]
#next_ = borders[0][1]
#c=0
#while next_ != init_:
#    for pair in borders:
#        p1, p2 = pair
#        if p1 == next_ and p2 != start:
#            start = next_
#            next_ =p2
#
#            break
#        
#        if p2 ==next_ and p1 != start:
#            start = next_
#            next_ = p1
#            break
#    c += 1
#    print(c)
#print(c)
    


