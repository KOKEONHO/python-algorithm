import collections
import re
from typing import List, Dict


class Solution:
    def solution_by_counter(self, paragraph: str, banned: List[str]) -> str:
        # Data Cleansing
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        # Counter
        counts: Dict[str, int] = collections.Counter(words)

        return counts.most_common(1)[0][0]


solution = Solution()

paragraph: str = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned: List[str] = ['hit']

print(solution.solution_by_counter(paragraph, banned))
