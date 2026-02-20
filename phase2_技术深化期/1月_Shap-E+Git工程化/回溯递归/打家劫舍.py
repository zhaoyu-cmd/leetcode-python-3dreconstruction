from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        pre_pre = nums[0]
        pre = max(nums[0], nums[1])
        for i in range(2, n):
            current = max(pre, pre_pre + nums[i])
            pre_pre = pre
            pre = current
        return pre