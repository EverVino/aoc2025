class Range:
    def __init__(self, inf, sup):
        self.inf = inf
        self.sup = sup
        self.valid = True

def open_data(path="test.txt"):
    with open(path, "r") as f:
        reader = f.read()

    ranges_section, _ = reader.split("\n\n")

    ranges = []
    for e in ranges_section.splitlines():
        i, f = e.split("-")
        ranges.append(Range(int(i),int(f)))

    ranges.sort(key= lambda x: (x.inf, x.sup))
    return ranges

counter = 0

ranges = open_data("input.txt")

n = len(ranges)
i = 0
j = 1
while j<n:
    actual = ranges[i]
    next_ = ranges[j]
    while actual.sup >= next_.inf and actual.sup >= next_.sup:
        next_.valid = False
        j +=1
        if j >= n:
            break
        next_ = ranges[j]
    
    if j >= n:
        break

    if actual.sup >= next_.inf:
        actual.sup = next_.inf -1
        if actual.sup <= actual.inf:
            actual.valid = False
    i = j
    j += 1

counter = 0
for e in ranges:
    if not e.valid:
        continue
    d = e.sup - e.inf +1 
    counter += d

print(counter)
