class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        combo = []

        def dfs():
            if len(combo) >= len(nums):
                res.append(combo[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in combo:
                    combo.append(nums[j])
                    dfs()
                    combo.pop()
                    
        dfs()

        return res