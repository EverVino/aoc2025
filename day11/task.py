def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()

    data ={}
    for line in reader:
        device_in, devices_out = line.split(':')
        data[device_in] = devices_out.split()

    return data

data = open_data('input.txt')

def bfs(data, node, target ):
    if node == target:
        return 1

    counter = 0

    for dest in data[node]:
        counter += bfs(data, dest, target)

    return counter

def get_all_paths(data, node, target):

    print(bfs(data, node, target))

get_all_paths(data, 'you', 'out')
