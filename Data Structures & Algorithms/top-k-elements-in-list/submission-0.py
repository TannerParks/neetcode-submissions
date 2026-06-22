class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        freq = {}
        heap = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            while len(heap) > k:
                heapq.heappop(heap)
         
        return [i[1] for i in heap]

