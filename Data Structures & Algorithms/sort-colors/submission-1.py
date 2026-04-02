class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        i = 0
        for x in range(len(counts)):
            for c in range(counts[x]):
                nums[i] = x
                i += 1
        
        return nums

