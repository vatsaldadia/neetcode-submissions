class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for idx in range(n):
            r_idx = (n - 1) - idx
            if idx == 0:
                max_left[idx] = height[0]
                max_right[r_idx] = height[-1]
            else:
                max_left[idx] = max(height[idx - 1], max_left[idx - 1])
                max_right[r_idx] = max(height[r_idx + 1], max_right[r_idx + 1])
        trapped = 0
        for idx in range(n):
            trapped += max(0, min(max_left[idx], max_right[idx]) - height[idx])
        # print(f"{max_left=}\n{max_right=}\n{trapped=}")
        return trapped