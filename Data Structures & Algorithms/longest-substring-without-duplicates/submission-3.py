class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s: return 0
        l = 0
        r = 0
        max_len = 0
        char_map = {}
        while r < len(s):
            # max_len = max(max_len, r - l)
            if s[r] in char_map:
                l = max(char_map[s[r]] + 1, l)
            char_map[s[r]] = r
            max_len = max(max_len, r - l +1)
            # print(f"{l=}, {s[l]=}, {r=}, {s[r]=}, {max_len=}, {char_map=}")
            r += 1
        return max_len
