from typing import List


class Solution:
    def solution_by_reverse(self, s: List[str]) -> None:
        s.reverse()

    def solution_by_two_pointer(self, s: List[str]) -> None:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def solution_by_slicing(self, s: List[str]) -> None:
        s = s[::-1]
        print(s)


solution = Solution()

s = ['안','녕','하','세','요']
solution.solution_by_slicing(s)