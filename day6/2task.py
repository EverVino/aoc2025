def open_data(path="test.txt"):
    with open(path, "r") as f:
        reader = f.read().splitlines()
    matrix = []
    for line in reader[:-1]:
        matrix.append(line) 
    operators = [e.strip() for e in reader[-1].split()]

    return operators, matrix

def get_sep(matrix):
    sep_idx = []
    num_idx = set()
    for line in matrix:
        for i, e in enumerate(list(line)):
            if not e.isnumeric():
                if i not in sep_idx and i not in num_idx:
                    sep_idx.append(i)
            else:
                num_idx.add(i)
                if i in sep_idx:
                    sep_idx.remove(i)
    return sep_idx

def get_new_matrix(matrix, sep):
    n = len(sep) + 2 
    m = len(matrix[0])
    new_sep = [-1] + sep + [m]
    n_matrix = [[] for _ in range(len(matrix))] 
    for i, line in enumerate(matrix):
        for j in range(n-1):
            n_matrix[i].append(line[new_sep[j]+1:new_sep[j+1]])

    return n_matrix

def get_ans_col(matrix, j, operator):
    n = len(matrix)
    m = len(matrix[0][j])

    acc = 1 if operator=="*" else 0
    for k in range(m):
        str_number = ""
        for i in range(n):
            str_number += str(matrix[i][j][k])
        if operator =="*":
            acc = acc*int(str_number)
        else:
            acc += int(str_number)
    return acc

operators, matrix = open_data("input.txt")
separators = get_sep(matrix)
n_matrix = get_new_matrix(matrix, separators)

cols = len(n_matrix[0])
rows = len(n_matrix)

acc = 0
for j in range(cols):
    operator = operators[j]
    ans = get_ans_col(n_matrix, j, operator)
    acc += ans
print(acc)
