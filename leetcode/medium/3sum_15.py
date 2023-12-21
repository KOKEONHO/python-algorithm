# class Solution:
#     def threeSum(self, nums):
#         result = []
#         nums.sort()
#
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 sum = nums[i] + nums[left] + nums[right]
#                 if sum > 0:
#                     right -= 1
#                     continue
#                 if sum < 0:
#                     left += 1
#                     continue
#                 result.append([nums[i], nums[left], nums[right]])
#
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#
#                 left += 1
#                 right -= 1
#
#         return result

class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                    continue
                if sum > 0:
                    right -= 1
                    continue

                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

        return result


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
