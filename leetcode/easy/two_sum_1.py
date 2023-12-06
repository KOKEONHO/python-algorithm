class Solution:
    def twoSum_by_brute_force(self, nums, target):
        for index in range(len(nums) - 1):
            num1 = nums[index]
            for sub_index in range(index + 1, len(nums)):
                num2 = nums[sub_index]
                if num1 + num2 == target:
                    result.append(index)
                    result.append(sub_index)
                    return result

    def twoSum_by_in_and_enumerate(self, nums, target):
        for index, number in enumerate(nums):
            complement = target - number

            if complement in nums[index + 1:]:
                return [index, nums[index + 1:].index(complement) + (index + 1)]

    def twoSum_by_dict(self, nums, target):
        nums_map = {}
        for index, number in enumerate(nums):
            nums_map[number] = index

        for index, number in enumerate(nums):
            if target - number in nums_map and index != nums_map[target - number]:
                return [index, nums_map[target - number]]

    def improved_twoSum_by_dict(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = []
print(solution.twoSum_by_in_and_enumerate(nums, target))
