class Solution(object):
    def maxTotalValue(self, nums, k):
        mx = float("-inf")
        mn = float("inf")
        for n in nums:
            mx = max(mx, n)
            mn = min(mn, n)
        return (mx-mn) * k
        # return (max(nums) - min(nums)) * k
