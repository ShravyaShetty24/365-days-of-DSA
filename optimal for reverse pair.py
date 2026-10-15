def merge(a, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if a[left] <= a[right]:
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            right += 1

    while left <= mid:
        temp.append(a[left])
        left += 1

    while right <= high:
        temp.append(a[right])
        right += 1

    for i in range(low, high + 1):
        a[i] = temp[i - low]


def countpair(a, low, mid, high):
    cnt = 0
    right = mid + 1

    for i in range(low, mid + 1):
        while right <= high and a[i] > 2 * a[right]:
            right += 1

        cnt += right - (mid + 1)

    return cnt


def merge_sort(a, low, high):
    cnt = 0

    if low >= high:
        return cnt

    mid = (low + high) // 2

    cnt += merge_sort(a, low, mid)
    cnt += merge_sort(a, mid + 1, high)

    cnt += countpair(a, low, mid, high)

    merge(a, low, mid, high)

    return cnt


def reversepair(a):
    return merge_sort(a, 0, len(a) - 1)


a = [5, 3, 2, 4, 1]

print(reversepair(a))