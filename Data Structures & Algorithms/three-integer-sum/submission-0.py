class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        ans = []
        nums = sorted(nums)
        for idx, i in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                triplet = [i, nums[left], nums[right]]
                if triplet not in ans and sum(triplet) == 0:
                    ans.append(triplet)
                elif sum(triplet) > 0:
                    right -= 1
                else:
                    left += 1
        return ans 