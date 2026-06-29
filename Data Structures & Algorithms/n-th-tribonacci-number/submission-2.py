class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        dp = [0, 1, 1]

        for i in range(3, n + 1):
            dp[i%3] = sum(dp)
        
        return dp[n%3]
