class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()

        for num in range(len(nums)):
            if nums[num] in number_set:
                return True
            number_set.add(nums[num])
        
        return False