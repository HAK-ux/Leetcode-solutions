class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { "]" : "[", "}": "{", ")" : "("}
        stack = []

        for bracket in s:
            if bracket in brackets:
                if not stack or stack.pop() != brackets[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        return stack == []
        # [()]
                    
