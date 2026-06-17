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
                if stack and stack[-1] == p_map[char]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False

    
            
