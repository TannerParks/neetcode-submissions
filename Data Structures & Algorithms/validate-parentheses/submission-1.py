class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in "([{":
                stack.append(p)
                continue
            if not stack:
                return False
            top = stack.pop()
            if p == ")" and top != "(":
                return False
            elif p == "]" and top != "[":
                return False
            elif p == "}" and top != "{":
                return False
            
        return not stack
                