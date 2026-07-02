arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

union = list(set(arr1 + arr2))
union.sort()

print(union)