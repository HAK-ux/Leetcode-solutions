class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        searchArray = []
        for arr in matrix:
            if target <= arr[-1]:
                searchArray = arr
                if target == arr[-1]:
                    return True
                break
        
        return self.binarySearch(searchArray, 0, len(searchArray) - 1, target)


    
    def binarySearch(self, arr, L, R, target):

        
        while L <= R:
            m = L + (R - L) // 2
            if target > arr[m]:
                L = m + 1
            elif target < arr[m]:
                R = m - 1
            elif target == arr[m]:
                return True
        
        return False
        
        
        
            