class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        n = len(nums)
        # for i in range(2*n):
        #     if i<n:
        #         ans[i] = nums[i]
        #         i +=1
        #     if i>=n:
        #         ans[i + n] = nums[i]
        return ans