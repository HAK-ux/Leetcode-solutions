class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                counts[0] += 1
            elif nums[i] == 1:
                counts[1] += 1
            elif nums[i] == 2:
                counts[2] += 1
        
        i = 0
        for x in range(len(counts)):
            for c in range(counts[x]):
                nums[i] = x
                i += 1
        
        return nums

