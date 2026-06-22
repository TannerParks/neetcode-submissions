class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_container = 0

        for i in range(len(heights)):
            dist = right - left
            min_height = min(heights[left], heights[right])
            water = min_height * dist
            max_container = max(max_container, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_container