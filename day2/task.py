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
        if len(number)%2 == 0:
            m = len(number)//2
            if number[:m]==number[m:]:
                acc += n
print(acc)

