import numpy as np
def open_data(path='input.txt'):
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
#    print('--------')
#    print(light)
#    print(combinations)
    return len(combinations[0]) if combinations else 0

data = open_data()
acc = 0
#machine = data[1]
#light = machine['light']
#wirings = machine['wiring']
#print('wirings')
#print(wirings)
#min_value = get_min_combinations(light, wirings)
#print(min_value)
for machine in data:
    light = machine['joltage']
    wirings = machine['wiring']
    min_value = get_min_combinations(light, wirings)
    print(min_value)
    acc += min_value
print(acc)
