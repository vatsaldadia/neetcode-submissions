class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                # print(f"found at {nums[i]}")
                return sorted([i, diff[nums[i]]])
            else:
                diff[target - nums[i]] = i