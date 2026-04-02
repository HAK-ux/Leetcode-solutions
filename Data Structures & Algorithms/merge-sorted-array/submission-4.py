class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0


        while l < m+n and r < n:
            if nums1[l] <= nums2[r]:
                l += 1
            else:
                nums1.insert(l, nums2[r])
                r += 1
            

        for i in range(n):
            nums1.pop()
        
        while r < n:
            nums1.append(nums2[r])
            r += 1