class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)

        prev = [1] * len(nums)
        post = [1] * len(nums)

        i = 1
        j = len(nums) - 2

        while (i < len(nums)):
            prev[i] = prev[i-1] * nums[i-1]
            i += 1
        while (j > -1):
            post[j] = post[j+1] * nums[j+1]
            j -= 1
        for i in range(len(answer)):
            answer[i] = prev[i] * post[i]

        return answer