class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1    
