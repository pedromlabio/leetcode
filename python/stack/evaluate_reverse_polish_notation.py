class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def isNumber(number: str):
            for char in number:
                if not (char.isdigit() or (char == "-" and len(number) > 1)): return False
            return True

        for token in tokens:
            if isNumber(token):
                stack.append(int(token))
            else:
                print(token)
                result = 0
                v2 = stack.pop()
                v1 = stack.pop()
                if token == "+": 
                    result = v1 + v2
                if token == "-": 
                    result = v1 - v2
                if token == "*": 
                    result = v1 * v2
                if token == "/":
                    result = v1 / v2
                stack.append(int(result))
        
        return stack.pop()