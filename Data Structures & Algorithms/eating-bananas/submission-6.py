class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = max(piles)
        while left <= right:
            mid = (left + right) // 2
            # print(f"{left=}, {right=}, {mid=}")
            hours_taken = 0
            for i in piles:
                hours_taken += math.ceil(float(i) / mid)
                # print(f"{hours_taken=}, {i=}, {mid=}")
            if hours_taken <= h:
                # print(f"{mid=}, {hours_taken=}")
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_speed            