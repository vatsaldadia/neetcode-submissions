class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_count_s = defaultdict(int)
        letter_count_t = defaultdict(int)
        for char in s:
            letter_count_s[char] += 1
        for char in t:
            letter_count_t[char] += 1
        for char in letter_count_s:
            if char not in letter_count_t:
                return False
            if letter_count_s[char] != letter_count_t[char]:
                return False
        return True