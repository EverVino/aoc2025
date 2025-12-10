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
                value = 'S' 
            elif s == '^':
                value = '^' 
            matrix[i].append(value)

    return matrix, start_point

matrix, start_point = open_data('input.txt')

# Add first beam
x, y = start_point
print(x, y)

matrix[x+1][y] = 1
cols = len(matrix[0])
rows = len(matrix)

for idx in range(2,rows):
    jdx = 0
    while jdx < cols: 
        e = matrix[idx][jdx]
        up_ = matrix[idx-1][jdx]
        if e == '^' and isinstance(up_,int) and up_ > 0 :
            matrix[idx][jdx-1] += up_ 
            matrix[idx][jdx+1] += up_ 
        
        if isinstance(up_, int) and up_>0 and up_ !='^' and e != '^':
            matrix[idx][jdx] += up_

        jdx += 1

print(sum(matrix[-1]))





