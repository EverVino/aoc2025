import numpy as np
import sympy as sp

def open_data(path='input.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()
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


def solve_with_parameters(variables, expanded_matrix):
    equations = expanded_matrix.shape[0]
    variables = expanded_matrix.shape[1] - 1
    C = np.atleast_2d(expanded_matrix[:, -1]).T
    features = expanded_matrix[:, : -1]

    parameters = variables - equations

    A = np.array(features[:,: equations], dtype=int)
    B = np.array(features[:, equations :], dtype=int)
    
    if np.linalg.det(A) == 0:
        B = np.array(features[:,: -equations], dtype=int)
        A = np.array(features[:, -equations :], dtype=int)
    max_value = C.max()

    min_sum = float("inf")
    try:
        A_inv = np.linalg.inv(A)
    except Exception as e:
        print("expanded matrix with error")
        print(expanded_matrix)
        print(e)
        return 0
    for value in set_values(parameters, max_value):
        if value.sum() > min_sum:
            continue
        M = C - B@value
        res = A_inv@M
            #res = np.linalg.solve(A.astype("float64"), M.astype("float64"))

        if (res < 0).any():
            continue

        rA=np.round(A, decimals=2).astype(int)
        valid = (rA -A).sum() < 1e-5

        if not valid:
            continue

        partial_sum = np.sum(res) + value.sum() 
        if partial_sum < min_sum:
            min_sum = partial_sum

    return min_sum

def get_min_value(i, light, wirings):
    no_sum = [20, 30, 92, 105, 114]
    no_process = [7, 41, 47, 73, 102]
    if i in (no_sum + no_process):
        return i, 0 

    variables = wirings.shape[0]

    A = wirings.T
    C = np.atleast_2d(light).T

    M = np.append(A,C, axis=1)
    Mref= sp.Matrix(M).echelon_form()
    Mnp = np.array(Mref)
    mask = ~np.all(Mnp==0, axis=1)

    Mf = Mnp[mask,:]

    return i, solve_with_parameters(variables, Mf)

data = open_data()
#acc = 0
#machine = data[1]
#light = machine['joltage']
#wirings = machine['wiring']
#value = get_min_value(light, wirings)
#print(value)

from joblib import Parallel, delayed, parallel_backend

total = 0
with parallel_backend('loky', n_jobs=19):
    for result in Parallel(return_as='generator')(
            delayed(get_min_value)(i, machine['joltage'], machine['wiring']) for i, machine in enumerate(data)
            ):
        total += result[1]

        print(result[0], result[1])

print(total)
