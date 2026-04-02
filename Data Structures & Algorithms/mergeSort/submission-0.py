# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        e = len(pairs)-1
        m = e//2
        list1 = self.mergeSort(pairs[0:m+1])
        list2 = self.mergeSort(pairs[m+1:e+1])

        sortedList = self.merge(list1, list2)

        return sortedList
    

    def merge(self, l1, l2):
        p1, p2 = 0, 0
        result = []
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1].key <= l2[p2].key:
                result.append(l1[p1])
                p1 += 1
            else:
                result.append(l2[p2])
                p2 += 1
        
        if p1 == len(l1):
            result.extend(l2[p2:])
        else:
            result.extend(l1[p1:])

        
        return result

