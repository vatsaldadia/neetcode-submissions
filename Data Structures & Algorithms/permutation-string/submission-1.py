class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter_s1 = Counter(s1)
        # counter_s1_copy = counter_s1.copy()
        counter_s2 = Counter(s2)
        # print(f"{counter_s1=}, {counter_s2=}")
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            temp_counter = Counter(s2[left : right + 1])
            if temp_counter == counter_s1:
                return True
            left += 1
            right += 1
        return False