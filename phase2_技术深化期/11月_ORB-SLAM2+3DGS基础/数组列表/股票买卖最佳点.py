class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return
        dp0=0
        dp1=-prices[0]
        for price in prices[1:]:
            new_dp0=max(dp0,dp1+price)#没有或者是卖了
            new_dp1=max(dp1,dp0-price)#前一天买了或者今天刚买
            dp0=new_dp0
            dp1=new_dp1
        return dp0