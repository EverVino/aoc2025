
def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()
    cols = len(reader[0])
    rows = len(reader)

    matrix = [[0 for _ in range(cols)] for __ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if reader[i][j] == '@':
                matrix[i][j] =1
    return matrix

def count_rolls(x,y, matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    vp = []
    for d in directions:
        new_x, new_y = x+d[0], y+ d[1]
        if 0 <= new_x < cols and 0<=new_y<rows:
            vp.append((new_x,new_y))

    c = 0
    for p in vp:
        i,j = p[0], p[1]
        c += matrix[i][j]
    return c


matrix = open_data('input.txt')
cols = len(matrix[0])
rows = len(matrix)
counter = 0

while True:
    new_counter = 0
    for i in range(rows):
        for j in range(cols):
            if not matrix[i][j]:
                continue
            n = count_rolls(i,j,matrix)
            if n <4:
                new_counter += 1
                matrix[i][j]=0
    if new_counter < 1:
        break
    counter += new_counter

print(counter)

