class Solution(object):
    def climbStairs(self, n):
        memo = {}
        return self.climb_stairs_helper(n, memo)

    def climb_stairs_helper(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.climb_stairs_helper(n-1, memo) + self.climb_stairs_helper(n-2, memo)
        return memo[n]