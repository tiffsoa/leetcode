class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for digit in digits:
            s += str(digit)
            incremented = int(s) + 1
        
        final_list = map(int, str(incremented))

        return final_list