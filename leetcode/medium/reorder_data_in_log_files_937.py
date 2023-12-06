from typing import List


class Solution:
    def solution_by_lambda(self, logs: List[str]) -> List[str]:
        digits: List[str] = list()
        letters: List[str] = list()
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
                continue
            letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


solution = Solution()
logs: List[str] = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(solution.solution_by_lambda(logs))
