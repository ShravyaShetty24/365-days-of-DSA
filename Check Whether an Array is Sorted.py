arr = [1, 2, 3, 4, 5]

sorted_array = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("Array is Sorted")
else:
    print("Array is Not Sorted")