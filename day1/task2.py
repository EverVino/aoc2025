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

counter = 0
state = 50
for step in data:
    direction, points = step
    while points > 100:
        points = points - 100
        counter +=1
    if direction == "R":
        if state+points <= 99:
            state = state + points
        else:
            counter += 1 if state != 0 and (state+points-100) != 0 else 0
            state = state +points -100
    else:
        if state-points >=0:
            state = state-points
        else:
            counter += 1 if state !=0 and (state-points+100) != 0 else 0
            state = state - points +100
    if state == 0:
        counter += 1
print(counter)
        # 50 + 50 = 100 -> 100 - 99 = 1
        # 50 - 51 = -1 -> -1 + 99 = 98
