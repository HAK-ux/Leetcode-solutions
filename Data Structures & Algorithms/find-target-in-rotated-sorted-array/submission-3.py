class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Determine if we are in the right or left half
        ## l, r, m
        ## if in left
        ##      is target more or less than current middle, if more then l = m + 1, if less then
        ##      then check if the target is more or less than the 0 index value (left half), if more, then taht means
        ##      search the left half -> r = m - 1, otherwise, search right half, l = m + 1
        ## if in right
        ##      if target is less than the current middle, search left half -> r = m - 1
        ##      if more than the current middle, find the last (-1) value, if less than that, check right half -> l = m +1
        ##      if more than that, check left half, r = m - 1

        l, r = 0, len(nums) - 1
        

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            
            # Left half
            if nums[l] <= nums[m]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Right half
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        

