class Solution:
    def climbStairs(self, n: int) -> int:
        step=0
        steps=1
        for i in range(n):
            step,steps=steps,step+steps
        return steps
