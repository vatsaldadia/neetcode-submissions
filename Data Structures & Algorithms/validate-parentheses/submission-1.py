class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop(-1)
                if popped == '(' and i != ')':
                    return False
                if popped == '{' and i != '}':
                    return False
                if popped == '[' and i != ']':
                    return False
        return len(stack) == 0