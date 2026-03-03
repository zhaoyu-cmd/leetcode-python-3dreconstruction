class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_dp=max_sum=nums[0]
        for num in nums[1:]:#这个地方注意一下不是只可以使用range(len(nums))，还可以直接遍历元素
            
            current_dp=max(num,current_dp+num)
        
            max_sum=max(current_dp,max_sum)
        return max_sum