class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start = 0
        freq = set()

        for end in range(len(nums)):
            num = nums[end]
            if (end - start) > k:
                start_num = nums[start]
                freq.remove(start_num)
                start += 1
            if num in freq:
                return True
            freq.add(num)
        
        return False