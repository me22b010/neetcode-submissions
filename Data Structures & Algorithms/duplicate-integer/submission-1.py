class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = list(set(nums))
        if len(l1) == len(nums):
            return False
        else:
            return True
        