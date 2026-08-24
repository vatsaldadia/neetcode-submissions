class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        # for idx, height in enumerate(heights):
        while left < right:
            length = (right - left)
            width = min(heights[left], heights[right])
            area = max(area, length * width)
            if heights[left] < heights[right]: 
                left += 1
            else:
                right -= 1
        return area