class Solution:
    def isValid(self, s: str) -> bool:
        para_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in para_map.values():
                stack.append(char)
            elif char in para_map.keys():
                if stack and stack[-1] == para_map[char]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False

