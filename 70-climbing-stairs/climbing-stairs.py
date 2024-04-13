class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [1,1,2]
        for i in range(3,n+1):
            mem.append(mem[i-2] + mem[i-1])
        return mem[n]
        