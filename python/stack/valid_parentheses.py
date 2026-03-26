class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "{" or char == "[" or char == "(":
                #push
                stack.append(char)
            else:
                if len(stack) == 0: return False
                #closing
                v = stack.pop()
                if not( (v == "(" and char == ")") or (v == "[" and char == "]") or (v == "{" and char == "}")): return False

        return len(stack) == 0       
