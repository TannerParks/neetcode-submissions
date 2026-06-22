class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]

        for num in nums:
            if num != res:
                count -= 1

                if count < 0 :
                    count = 0
                    res = num
            else:
                count += 1
        
        return res