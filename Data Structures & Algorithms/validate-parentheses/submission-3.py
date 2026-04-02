class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for bracket in s:
            if bracket == "{" or bracket ==  "(" or bracket == "[":
                brackets.append(bracket)
            elif bracket == "}":
                if brackets == [] or brackets.pop() != "{":
                    return False
            
            elif bracket == "]":
                if brackets == [] or brackets.pop() != "[":
                    return False

            elif bracket == ")":
                if brackets == [] or brackets.pop() != "(":
                    return False
        return brackets == []
            
            

