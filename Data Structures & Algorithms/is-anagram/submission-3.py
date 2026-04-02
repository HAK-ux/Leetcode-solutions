class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}
        for ch in s:
            if ch in seen:
                seen[ch] +=1
            else:
                seen[ch] = 0
        for ch in t:
            if ch in seen2:
                seen2[ch] +=1
            else:
                seen2[ch] = 0
        return seen == seen2 


        