class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr=[], mask=[False] * len(nums)):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not mask[i]:
                    curr.append(nums[i])
                    mask[i] = True
                    dfs(curr, mask)
                    curr.pop()
                    mask[i] = False
        
        dfs()

        return res