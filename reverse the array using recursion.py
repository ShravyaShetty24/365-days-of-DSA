# Reverse array/string using recursion
def reverse(arr, l, r):
    if l >= r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]   # swap
    reverse(arr, l + 1, r - 1)
arr = [1, 2, 3, 4, 5]
reverse(arr, 0, len(arr) - 1)
print("Reversed List:", arr)

# Example with string
s = list("python")
reverse(s, 0, len(s) - 1)
print("Reversed String:", "".join(s))