arr = [4, 5, 1, 2, 1, 2, 4]

for i in arr:
    if arr.count(i) == 1:
        print("First Non-Repeating Element =", i)
        break