def subarray(arr,k):
    xor=0
    count=0
    freq={0:1}
    for num in arr:
        xor^=num
        required=xor^k
        count+=freq.get(required,0)
        freq[xor]=freq.get(xor,0)+1
    return count
arr=[4,2,2,6,4]
k=6
print(subarray(arr,k))