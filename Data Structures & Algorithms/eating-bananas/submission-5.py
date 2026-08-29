class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        min_speed = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            print(f"{left=}, {right=}, {mid=}")
            if mid <= 0:
                break
            hours_taken = 0
            for i in piles:
                hours_taken += math.ceil(i / mid)
                # print(f"{hours_taken=}, {i=}, {mid=}")
            if hours_taken > h:
                left = mid + 1
            if hours_taken <= h:
                # print(f"{mid=}, {hours_taken=}")
                min_speed = min(mid, min_speed)
                right = mid
        return min_speed            