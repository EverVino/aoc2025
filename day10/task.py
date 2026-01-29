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

        machine['light'] = new_light
        machine['wiring'] = buttons 
        machine['joltage'] = joltage

        data.append(machine)
    return data 

def sum2list(lst1, lst2):
    result = []
    for x1, x2 in zip(lst1,lst2):
        r = x1 + x2 if x1 +x2<2 else 0
        result.append(r)

    return result

def get_min_combinations(light, wirings):
    combinations = []
    def get_combination(light, wirings, combination, total_sum):
        if light == total_sum:
            combinations.append(combination.copy())
            return
        if not wirings:
            return
        n = len(wirings)
        for i in range(n):
            t_sum = sum2list(total_sum,wirings[i])
            combination.append(wirings[i])
            get_combination(light, wirings[i+1:], combination, t_sum.copy())
            combination.pop()
    
    total_sum = [0 for _ in range(len(light))]

    get_combination(light, wirings, [], total_sum)
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
    light = machine['light']
    wirings = machine['wiring']
    min_value = get_min_combinations(light, wirings)
    acc += min_value
print(acc)
