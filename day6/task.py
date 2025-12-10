def open_data(path="test.txt"):
    with open(path, "r") as f:
        reader = f.read().splitlines()
    matrix = []
    print(len(reader))
    print("----------")
    c = 0
    for line in reader[:-1]:
        c += 1
        print(c)
        matrix.append([int(number.strip()) for number in line.split()])

    matrix.append([number.strip() for number in reader[-1].split()])

    return matrix
matrix = open_data("input.txt")

rows = len(matrix) -1 
cols = len(matrix[0])
operators = matrix[-1]

col_result = 0
for j in range(cols):
    operator = operators[j]
    acc = 0 if operator=="+" else 1
    for i in range(rows):
        if operator == "+":
            acc += matrix[i][j]
        else:
            acc *= matrix[i][j]
    col_result += acc 

print(col_result)

