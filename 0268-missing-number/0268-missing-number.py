class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if(len(nums)>10000):
            return False    
        nums=sorted(nums)
        for i in range(len(nums)):
            if(nums[i]!=i):
                break
            if (len(nums)):
                i= i+1    
        return i