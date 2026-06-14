class Solution:
    def secondLargestElement(self, nums):
        largest=nums[0]
        slargest=-1
        for i in range(1,len(nums)):
            if nums[i]>largest:
                slargest=largest
                largest=nums[i] 
            elif nums[i]<largest and nums[i]>slargest:
                slargest=nums[i]
        return slargest   
nums=[1,2,3,5,1]
c=Solution()
print(c.secondLargestElement(nums))