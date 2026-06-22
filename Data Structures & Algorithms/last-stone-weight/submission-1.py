import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-s for s in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)

            if x < y:
                heapq.heappush(new_stones, x-y)
            else:
                continue
        
        if new_stones:
            return -new_stones[0]
        return 0
