# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    

    def mergeSortHelper(self, pairs: List[Pair], s, e):
        if e - s + 1 <= 1:
            return pairs

        m = (s+e)//2
        
        # Sort Left Half
        self.mergeSortHelper(pairs, s, m)

        # Sort Right Half
        self.mergeSortHelper(pairs, m+1, e)
        
        # Merge Sorted Halves
        self.merge(pairs, s, m, e)


        return pairs


    
    def merge(self, pairs, s, m, e):
        # Left Half
        L = pairs[s:m+1]

        # Right Half
        R = pairs[m+1:e+1]

        lp, rp = 0, 0
        
        i = s # start index for array
        while lp < len(L) and rp < len(R):
            if L[lp].key <= R[rp].key:
                pairs[i] = L[lp]
                lp += 1
            else:
                pairs[i] = R[rp]
                rp += 1
            
            i += 1

        while lp < len(L):
            pairs[i] = L[lp]
            lp += 1
            i += 1
        
        while rp < len(R):
            pairs[i] = R[rp]
            rp += 1
            i += 1
        

        



