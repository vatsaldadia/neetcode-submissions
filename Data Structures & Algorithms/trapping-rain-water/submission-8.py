class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        max_left = height[0]
        right = n - 1
        max_right = height[-1]
        trapped = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(height[left], max_left)
                trapped += max(0, max_left - height[left])
            else:
                right -= 1
                max_right = max(height[right], max_right)
                trapped += max(0, max_right - height[right])
            # print(f"{left=}, {right=}, {trapped=}, {max_left=}, {max_right=}")
        return trapped