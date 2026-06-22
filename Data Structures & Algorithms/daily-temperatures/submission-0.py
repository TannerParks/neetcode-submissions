class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while temps and temp > temps[-1][1]:
                low = temps.pop()[0]
                res[low] = idx - low
            
            temps.append((idx, temp))
        
        return res