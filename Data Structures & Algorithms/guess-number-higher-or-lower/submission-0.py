# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while True:
            num = (lo + hi) // 2
            res = guess(num)

            if res < 0:
                hi = num
            elif res > 0:
                lo = num + 1
            else:
                return num
