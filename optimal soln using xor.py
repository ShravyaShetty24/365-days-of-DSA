def single_no(arr):
    xor=0
    for i in range(len(arr)):
        xor=xor^arr[i]
    return xor
arr=[1,1,2,3,3,4,4]
print(single_no(arr))