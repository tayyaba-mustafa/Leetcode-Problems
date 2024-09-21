class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_moves = sum(nums) - len(nums) * min(nums)
        return min_moves