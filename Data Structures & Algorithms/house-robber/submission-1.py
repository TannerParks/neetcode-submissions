class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        one = nums[0]
        two = max(one, nums[1])

        for i in range(2, len(nums)):
            one, two = two, max(two, one + nums[i])
        
        return two