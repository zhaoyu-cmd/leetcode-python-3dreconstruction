class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        pre_pre=1
        pre=2
        curent=0
        for i in range(3,n+1):
            curent=pre_pre+pre
            pre_pre=pre
            pre=curent
        return curent
            

            