def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()

    return reader

data = open_data('input.txt')
acc = 0

for e in data:
    max_value = 0
    for i in range(len(e)-1):
        for j in range(i+1,len(e)):
            value = int(e[i]+e[j])
            if value > max_value:
                max_value = value
    acc += max_value

print(acc)


