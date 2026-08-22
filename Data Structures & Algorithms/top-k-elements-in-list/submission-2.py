class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_occurence = len(nums) - (len(set(nums)) - 1)
        buckets = [(i + 1) for i in range(max_occurence)]
        numbers = []
        for _ in range(max_occurence):
            numbers.append([])
        for num, count in Counter(nums).items():
            numbers[count - 1].append(num)
        ans = []
        while k > 0:
            last_list = numbers.pop(-1)
            ans.extend(last_list)
            k -= len(last_list)
        return ans