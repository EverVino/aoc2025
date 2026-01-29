import numpy as np

def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()
    lights = []
    joltages = []
    wirings = []
    data = []
    for line in reader:
        machine = {}
        raw = line.split()
        light = list(raw[0][1:-1])
        raw_wiring = raw[1:-1]
        wiring = []
        for w in raw_wiring:
            nw = [int(e) for e in w[1:-1].split(',')]
            wiring.append(nw)
        
        joltage = [int(e) for e in raw[-1][1:-1].split(',')]

        buttons = []
        n = len(light)
        for nws in wiring:
            button = [0 for _ in range(n)]
            for nw in nws:
                button[nw] = 1
            buttons.append(button)
        new_light = []
        for e in light:
            if e == '#':
                new_light.append(1)
            else:
                new_light.append(0)

        machine['light'] = np.array(new_light)
        machine['wiring'] = np.array(buttons)
        machine['joltage'] = np.array(joltage)

        data.append(machine)
    return data 

def sum2list(lst1, lst2):
    return lst1 + lst2 

def is_valid_yet(light, total_sum):
    comparison = total_sum > light
    return not comparison.any()
    
def get_min_combinations(light, wirings):
    combinations = []

    def get_combination(idx, light, wirings, combination, total_sum):
        if np.array_equal(light, total_sum):
            combinations.append(combination.copy())
            return
        if not is_valid_yet(light, total_sum):
            return
        if idx >= wirings.shape[0]:
            return

        combination.append(wirings[idx])
        t_sum = sum2list(total_sum,wirings[idx])
        get_combination(idx, light, wirings, combination, t_sum.copy())
        combination.pop()
        get_combination(idx+1, light, wirings, combination, total_sum.copy())

    
    total_sum = [0 for _ in range(len(light))]

    get_combination(0, light, wirings, [], total_sum)
    combinations.sort(key=lambda x: len(x))
    return len(combinations[0]) if combinations else 0

def set_values(n, max_value, values_list=[]):
    if len(values_list) >= n:
        yield np.atleast_2d(values_list).T
        return
    for i in range(max_value):
        values_list.append(i)
        yield from set_values(n, max_value, values_list)
        values_list.pop()

def solve_nxn(light, wirings):
    A = wirings.T
    C = np.atleast_2d(light).T
    res = np.linalg.solve(A,C)
    return res.sum()

def solve_mxn(light, wirings):
    n = light.shape[0]
    m = wirings.shape[0]
    A = wirings.T
    C = np.atleast_2d(light).T

    B = np.append(A,C, axis=1)
    Bexp  = np.unique(B, axis=0)
    M = Bexp[:,:-1]
    b = Bexp[:,[-1]]
    print(Bexp.shape[0])
    print(Bexp)
    print("----------")
    print(M)
    print(b)
    print("deter")
    print(np.linalg.det(M))
    if M.shape[0] == b.shape[0]:
        res = np.linalg.solve(M,b)
        return res.sum()
    if M.shape[0] < b.shape[0]:
        return solve_nxm(b.T, M.T)


def solve_nxm(light, wirings):
    n = light.shape[0]
    m = wirings.shape[0]
    xn = m - n
    A = np.array(wirings[-n:])
    B = np.array(wirings[:-n])
    max_value = light.max()
    At = A.T
    Bt = B.T
    Ct = np.atleast_2d(light).T
    min_sum = float("inf")

    for value in list(set_values(xn, max_value)):
        M = Ct - Bt@value
        res = np.linalg.solve(At, M)
        if (res < 0).any():
            continue
        if (res != res.astype(int)).any():
            continue

        partial_sum = res.sum() + value.sum() 
        if partial_sum < min_sum:
            min_sum = partial_sum

    return min_sum

def get_min_value(light, wirings):
    n = light.shape[0]
    m = wirings.shape[0]
    xn = m-n
    if xn == 0:
        return solve_nxn(light, wirings)
    elif xn < 0:
        return solve_mxn(light, wirings)
    elif xn > 0:
        return solve_nxm(light, wirings)

data = open_data()
acc = 0
machine = data[2]
light = machine['joltage']
wirings = machine['wiring']
value = get_min_value(light, wirings)
print(value)
#get_min_value(light, wirings)
#min_value = get_min_combinatioplitss(light, wirings)

#print(min_value)
#for machine in data:
#    light = machine['joltage']
#    wirings = machine['wiring']
#    min_value = get_min_combinations(light, wirings)
#    print(min_value)
#    acc += min_value
print(acc)
