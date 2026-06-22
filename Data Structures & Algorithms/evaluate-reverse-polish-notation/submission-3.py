class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token != '+' and token != '-' and token != '/' and token != '*':
                s.append(int(token))
                continue
            op1 = s.pop()
            op2 = s.pop()
            if token == '+':
                s.append(int(op2 + op1))
            elif token == '-':
                s.append(int(op2 - op1))
            elif token == '/':
                s.append(int(op2 / op1))
            elif token == '*':
                s.append(int(op2 * op1))
        
        return s.pop()
