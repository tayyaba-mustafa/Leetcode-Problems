class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ele = min(nums)
        min_moves = sum(nums) - len(nums) * min_ele
        return min_moves