class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for index in range(len(s) - 1):
            result = max(result,
                         expand(index, index + 1),
                         expand(index, index + 2),
                         key=len)

        return result


solution = Solution()
s = 'babad'
print(solution.longestPalindrome(s))
