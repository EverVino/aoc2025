def open_data(input="test.txt"):
    steps = []
    with open(input, "r") as f:
        reader = f.readlines()
    for e in reader:
        x = e[:1]
        y = int(e[1:].strip())
        steps.append((x,y))
    return steps

data = open_data("input.txt")

LIMITS = (1,99)
counter = 0
state = 50
for step in data:
    direction, points = step
    while points > 100:
        points = points - 100
    if direction == "R":
        state = (state+points) if (state+points)<=99 else (state+points-99-1)
    else:
        state = (state-points) if (state-points)>=0 else (state-points+99+1)
    if state == 0:
        counter += 1
print(counter)
        # 50 + 50 = 100 -> 100 - 99 = 1
        # 50 - 51 = -1 -> -1 + 99 = 98
