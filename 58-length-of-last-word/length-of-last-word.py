class Solution(object):
    def lengthOfLastWord(self, s):
        word=s.split()
        le=len(word[-1])
        return le
        