class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        left = 0
        right = 1
        max_height_seen = height[left]
        max_height_segment = height[right]
        max_height_segment_idx = right
        trapped = 0
        while right < len(height):
            # print(f"{left=}, {right=}, ", end='')
            # print(f"{trapped=}, {max_height_segment_idx=}")
            if height[right] >= height[left]:
                left = right
                right += 1
                max_height_seen = height[left]
                if right != len(height):
                    max_height_segment = height[right]
                    max_height_segment = height[right]
                    max_height_segment_idx = right
            else:
                trapped += height[left] - height[right]
                if max_height_segment <= height[right]:
                    max_height_segment = height[right]
                    max_height_segment_idx = right
                right += 1
        # print(f"{left=}, {right=}, ", end='')
        # print(f"{trapped=}, {max_height_segment_idx=}")
        for idx in range(left + 1, len(height)):
            if idx <= max_height_segment_idx:
                trapped -= height[left] - max_height_segment
            else:
                trapped -= height[left] - height[idx]
            # print(f"{idx=}, {trapped=}")
        return trapped


