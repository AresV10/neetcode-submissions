class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #{')':'(', '}':'{', ']':'['}
        parentheses = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif not stack or char != parentheses[stack.pop()]:
                return False
        return not stack