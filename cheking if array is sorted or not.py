class Solution:
    def isSorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
nums=list(map(int,input("enter the elements:").split()))
s=Solution()
print(s.isSorted(nums))