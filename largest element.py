class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for i in range(1,len(nums)): 
            if nums[i]>largest:
                largest=nums[i]
        return largest       
nums=[1,2,4,7,7,5]
s=Solution()
print(s.largestElement(nums))