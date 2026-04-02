class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        match = {"]": "[", "}": "{", ")": "("}
        for bracket in s:
            if bracket in match:
                if brackets == [] or brackets.pop() != match[bracket]:
                    return False
            else:
                brackets.append(bracket)
        return brackets == []
            
            

