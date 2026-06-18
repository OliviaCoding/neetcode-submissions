class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char in p_map.values():
                stack.append(char)

            elif char in p_map:
                if not stack or p_map[char] != stack[-1]:
                    return False

                stack.pop()
            
            else:
                return False
        
        return not stack

