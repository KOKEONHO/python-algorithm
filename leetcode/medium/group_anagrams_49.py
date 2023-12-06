import collections
from typing import Dict, List


class Solution:
    def solution_by_dict_and_sorted(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return sorted(anagrams.values(), key=len)


solution = Solution()
strs: List[str] = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(solution.solution_by_dict_and_sorted(strs))
