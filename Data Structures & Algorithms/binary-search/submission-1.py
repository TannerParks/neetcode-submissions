class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        
        return -1