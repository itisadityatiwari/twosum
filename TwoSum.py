class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if(sum==target):
                    return i,j
        
sol=Solution()
print(sol.twoSum([1,3,4,6],7))