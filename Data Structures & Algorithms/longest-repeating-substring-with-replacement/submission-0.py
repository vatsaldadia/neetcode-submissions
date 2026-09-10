class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter(s)
        # print(count)
        l = 0
        r = 0
        maxlen = 0
        count = [0] * 26
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            while r - l + 1 > max(count) + k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
            r += 1
            # print(f"{l=}, {r=}, {maxlen=}\n{count=}")
        return maxlen