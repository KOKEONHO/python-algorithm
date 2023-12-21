class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


solution = Solution()
nums = [6, 2, 6, 5, 1, 2]
print(solution.arrayPairSum(nums))
