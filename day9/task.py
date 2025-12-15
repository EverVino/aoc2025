
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

n = len(data)

A = 0
for i in range(n):
    for j in range(i+1,n):
        a = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if abs(a) > A:
            A = abs(a)
print(A)
