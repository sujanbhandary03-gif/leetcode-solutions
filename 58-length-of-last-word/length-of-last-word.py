class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        w=s.split()
        return len(w[-1])