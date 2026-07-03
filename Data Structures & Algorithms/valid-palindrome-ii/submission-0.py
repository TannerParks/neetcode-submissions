class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(new_s: str) -> bool:
            left, right = 0, len(new_s) - 1
            while left < right:
                if new_s[left] != new_s[right]:
                    return False
                left += 1
                right -=1
            
            return True
        
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
            left += 1
            right -= 1
        
        return True