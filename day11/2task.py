from functools import cache

def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()

    data ={}
    for line in reader:
        device_in, devices_out = line.split(':')
        data[device_in] = devices_out.split()

    return data

data = open_data('input.txt')

@cache
def bfs(node, target, fft, dac) :
    if node == target:
        return 1 if fft and dac else 0
    fft = fft or node == 'fft'
    dac = dac or node == 'dac'
    counter = 0
    for dest in data[node]:
        counter += bfs(dest, target, fft, dac)

    return counter

def get_all_paths(data, node, target):

    path = []
    data = data
    print(bfs(node, target, False, False))

get_all_paths(data, 'svr', 'out')
