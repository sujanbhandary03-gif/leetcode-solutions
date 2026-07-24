class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start, max_len = 0, 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):

            left, length = expand(i, i)
            if length > max_len:
                start, max_len = left, length

            left, length = expand(i, i + 1)
            if length > max_len:
                start, max_len = left, length

        return s[start:start + max_len]