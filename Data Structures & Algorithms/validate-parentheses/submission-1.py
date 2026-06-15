class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in paren_dict:
                top_element = stack.pop() if stack else '#'

                if top_element != paren_dict[char]:
                    return False

            else:
                stack.append(char)

        return not stack


