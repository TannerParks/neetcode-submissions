class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}

        for idx in range(len(nums)):
            num = target - nums[idx]
            if num in num_dic:
                return [num_dic[num], idx]
            num_dic[nums[idx]] = idx