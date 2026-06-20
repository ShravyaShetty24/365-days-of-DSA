arr = [1, 1, 0, 1, 1, 1]

count = ans = 0

for x in arr:
    if x == 1:
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)