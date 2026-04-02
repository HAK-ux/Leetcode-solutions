class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1
        for ch in t:
            seen2[ch] = seen2.get(ch, 0) + 1
        
        return seen == seen2
        
    