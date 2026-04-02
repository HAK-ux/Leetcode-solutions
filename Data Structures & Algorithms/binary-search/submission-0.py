class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] < target:
                L = m + 1
            elif nums[m] > target:
                R = m - 1
            else:
                return m
            
        return -1


        # [1, 2, 3] target = 3
        # L = 2
        # R = 2
        # M = 1