class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nmums[j] == target, i!=j
        # find one number, find the complement after -> target - number

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

        return
        