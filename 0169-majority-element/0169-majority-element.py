class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        v = 0
        for num in nums:
            if v == 0:
                c = num
            if num == c:
                v +=1
            else:
                v -=1
        return c