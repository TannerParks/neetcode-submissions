class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        start = 0
        longest = 0

        for end in range(len(s)):
            curr = s[end]
            freq[curr] = freq.get(curr, 0) + 1

            while freq[curr] > 1:
                char = s[start]
                freq[char] -= 1

                if freq[char] == 0:
                    del freq[char]
                
                start += 1
            
            longest = max(longest, end - start + 1)
        
        return longest