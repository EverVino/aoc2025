def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read()
    data = []
    for e in reader.split(','):
        x, y = e.split('-')
        data.append((int(x),int(y)))
    return data


data = open_data('input.txt')
acc =0 
for e in data:
    for n in range(e[0],e[1]+1):
        number = str(n)
        ln = len(number)
        for i in range(1,ln//2+1):
            r = number[0:i]
            if len(number.replace(r,"")) == 0:
                acc += n
                break
print(acc)

