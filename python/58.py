class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.strip()
        list_s = new_s.split()

        return len(list_s[len(list_s)-1])