def open_data(path="test.txt"):
    with open(path, "r") as f:
        reader = f.read()

    ranges_section, ids_section= reader.split("\n\n")

    ranges = []
    for e in ranges_section.splitlines():
        i, f = e.split("-")
        ranges.append((int(i),int(f)))

    ids = [int(id) for id in ids_section.splitlines()]

    return ranges, ids

def check_valid(idx, ranges):
    for rn in ranges:
        if rn[0] <= idx <= rn[1]:
            return True 
    return False

ranges, ids = open_data("input.txt")
counter = 0

for idx in ids:
    if check_valid(idx, ranges):
        counter += 1

print(counter)


