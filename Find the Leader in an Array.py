arr = [16, 17, 4, 3, 5, 2]

max_right = arr[-1]
print(max_right, end=" ")

for i in range(len(arr)-2, -1, -1):
    if arr[i] > max_right:
        max_right = arr[i]
        print(max_right, end=" ")