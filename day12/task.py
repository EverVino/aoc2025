def read_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read()
    
    blocks = reader.split('\n\n')
    shapes = blocks[:-1]
    regions = blocks[-1]
    data = {}
    shape_areas = {}
    for shape in shapes:
        idx = int(shape.split()[0][0])
        counter = 0
        for line in shape.split():
            for e in line:
                if e == '#':
                    counter += 1
        shape_areas[idx] = counter

    region_data = []
    for region in regions.split('\n')[:-1]:
        raw_area, raw_presents = region.split(': ')
        x, y = raw_area.split('x')
        area = int(x)*int(y)
        presents = [int(e) for e in raw_presents.split()]
        elem = {'area': area, 'presents': presents}
        region_data.append(elem)

    return shape_areas, region_data


shapes, regions = read_data('input.txt')

acc = 0
for region in regions:
    total_area = region['area']
    areas = 0 
    for idx, present in enumerate(region['presents']):
        areas += shapes[idx]*present

    print('--------')
    print(areas)
    print()
    print(total_area)
    if 0.85*total_area > areas:
        acc += 1
print(acc)
        

