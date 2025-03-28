class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        prev = [1] * len(nums)
        post = 1
        i = 1
        j = len(nums) - 1
        while (i < len(nums)):
            prev[i] = prev[i-1] * nums[i-1]
            i += 1
        while (j > -1):
            answer[j] = post * prev[j]
            post *= nums[j]
            j -= 1
        return answer