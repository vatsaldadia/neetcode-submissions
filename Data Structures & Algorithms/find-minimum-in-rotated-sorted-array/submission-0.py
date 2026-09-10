class Solution:
    '''
    [5, 6, 1, 2, 3, 4]
    '''


    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # print(f"{left=}, {mid=}, {right=}")
            num_l, num_r, num_m = nums[left], nums[right], nums[mid]
            if num_m <= num_r and num_l <= num_m:
                return nums[left]
            elif num_m > num_r:
                left = mid + 1
            else:
                right = mid