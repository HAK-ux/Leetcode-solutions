class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # L, R = 0, len(nums) - 1

        # while L <= R:
        #     m = (L + R) // 2

        #     if nums[m] < target:
        #         L = m + 1
        #     elif nums[m] > target:
        #         R = m - 1
        #     else:
        #         return m
            
        # return -1
        return self.binary_search(0, len(nums) - 1, nums, target)


    def binary_search(self, L, R, arr, target):
        if L > R:
            return -1
        
        m = (L + R) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            return self.binary_search(m + 1, R, arr, target)
        elif arr[m] > target:
            return self.binary_search(L , m - 1, arr, target)
        




        # [1, 2, 3, 6, 7] target = 3
        # L = 2
        # R = 2
        # M = 1