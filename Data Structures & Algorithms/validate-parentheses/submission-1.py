class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ('(','{','['):
                stack.append(char)
            elif char in (')','}',']'):
                if stack:
                    corresponding_paren = stack.pop()
                else:
                    return False
                if corresponding_paren == '(' and char != ')':
                    return False
                elif corresponding_paren == '{' and char != '}':
                    return False
                elif corresponding_paren == '[' and char != ']':
                    return False
        return not stack