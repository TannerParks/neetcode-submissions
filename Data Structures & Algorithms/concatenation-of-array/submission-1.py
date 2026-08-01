class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = [0] * (len(nums) * 2)

        for i in range(len(nums)):
            concat[i], concat[i + len(nums)] = nums[i], nums[i]
        
        return concat