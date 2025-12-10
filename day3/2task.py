def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()

    return reader

data = open_data('input.txt')
acc = 0
def get_max_i(ini, end, L):

    max_n = int(L[ini])
    max_i = ini
    for i in range(ini, end+1):
       n = int(L[i])
       if n>max_n:
           max_n = n
           max_i = i
    return max_i, max_n

for e in data:
    max_value = 0
    idxs = []
    max_i = 0
    char_left = 12
    end_ = len(e) - char_left 
    init = max_i
    while len(idxs)<12:
        max_i, n = get_max_i(init, end_, e)
        init = max_i+1
        end_ += 1
        idxs.append(max_i)
    number = ""
    for idx in idxs:
        number = number + e[idx]

    acc += int(number)

print(acc)


