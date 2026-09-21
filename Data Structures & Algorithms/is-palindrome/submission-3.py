class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left < right) and (left < len(s)) and (right > 0):
            skipped = False
            if not s[left].isalnum():
                left += 1
                skipped = True
            if not s[right].isalnum():
                right -= 1
                skipped = True
            
            if not skipped:
                if s[left].lower() != s[right].lower():
                    # print(s[left], s[right])
                    return False
                left += 1
                right -= 1
        
        return True