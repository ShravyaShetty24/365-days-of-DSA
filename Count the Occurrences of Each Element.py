arr = [1, 2, 2, 3, 1, 4, 2]

visited = []

for i in arr:
    if i not in visited:
        print(i, "->", arr.count(i))
        visited.append(i)