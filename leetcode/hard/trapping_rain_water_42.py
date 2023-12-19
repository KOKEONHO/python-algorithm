class Solution:
    def trap_by_two_pointers(self, height):
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                volume += left_max - height[left]
                continue
            right -= 1
            right_max = max(right_max, height[right])
            volume += right_max - height[right]

        return volume

    def trap_by_stack(self, height):
        stack = []
        volume = 0

        for i in range(len(height)):
            # `stack`이 비어있지 않으면서 변곡점을 만났을 때
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * water
            stack.append(i)
        return volume


solution = Solution()
height = [4, 3, 2, 1, 0, 4, 5]
print(solution.trap_by_stack(height))
