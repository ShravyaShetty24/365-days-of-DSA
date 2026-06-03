def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)

n = 10
print_reverse(n)
