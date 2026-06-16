class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1
nums=list(map(int,input("enter the elements:").split()))
s=Solution()
k=s.removeDuplicates(nums)
print("unique elements are:",nums[:k])