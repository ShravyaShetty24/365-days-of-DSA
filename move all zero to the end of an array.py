arr = [0, 1, 0, 3, 12]

result = []

for i in arr:
    if i != 0:
        result.append(i)

while len(result) < len(arr):
    result.append(0)

print(result)