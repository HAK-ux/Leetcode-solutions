class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            m = L + (R - L) // 2
            if target <= matrix[m][-1] and target >= matrix[m][0]:
                return self.binarySearch(matrix[m], 0, len(matrix[m]) - 1, target)
            elif target > matrix[m][-1]:
                L = m + 1
            elif target < matrix[m][-1]:
                R = m - 1
            
        return False
        


    
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
        
        
        
            