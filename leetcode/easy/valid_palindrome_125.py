import collections
import re
from typing import Deque


class Solution:
    def solution_by_list(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def solution_by_deque(self, s: str):
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def solution_by_slicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]


solution = Solution()

s = "A man, a plan, a canal: Panama"
print(solution.solution_by_list(s))
print(solution.solution_by_deque(s))
print(solution.solution_by_slicing(s))
