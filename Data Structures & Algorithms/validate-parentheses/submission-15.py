class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', ']': '[', '}' : '{'}

        for bracket in s:
            if bracket in closeToOpen and stack and stack[-1] == closeToOpen[bracket]:
                stack.pop()
            elif bracket in closeToOpen and stack and stack[-1] != closeToOpen[bracket]:
                return False
            else:
                stack.append(bracket)
        
        return stack == []
