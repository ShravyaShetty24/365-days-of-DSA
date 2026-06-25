arr = [1, 2, 3, 2, 4, 2, 5]
x = 2

count = 0

for i in arr:
    if i == x:
        count += 1

print("Frequency =", count)