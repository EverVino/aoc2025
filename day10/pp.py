

def assign_values(n, threshold, values_list = []):
    if len(values_list) >= n:
        yield values_list.copy()
        return
    for i in range(n):
        values_list.append(i)
        yield from assign_values(n, threshold, values_list)
        values_list.pop()

for e in assign_values(3,3):
    print(e)
