def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()

    matrix = [[] for _  in range(len(reader))]
    start_point = None
    for i, line in enumerate(reader):
        for j, s in enumerate(line):
            value = 0
            if s == 'S':
                start_point=(i,j)
                value = 8 
            elif s == '^':
                value = 1
            matrix[i].append(value)

    return matrix, start_point

matrix, start_point = open_data('input.txt')

# Add first beam
x, y = start_point
print(x, y)

matrix[x+1][y] = 2
counter = 0
for idx in range(1,len(matrix)-1):
    for jdx in range(len(matrix[idx])):
        e = matrix[idx][jdx]
        if e == 1 and matrix[idx-1][jdx] == 2:
            matrix[idx][jdx-1] = 2
            matrix[idx][jdx+1] = 2
            matrix[idx+1][jdx-1] = 2
            matrix[idx+1][jdx+1] = 2

        if e == 2 and matrix[idx+1][jdx] != 1:
            matrix[idx+1][jdx] = 2

print(counter)




