class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                res = 0
                if i == "+":
                    res = num1 + num2
                elif i == "-":
                    res = num1 - num2
                elif i == "*":
                    res = num1 * num2
                else:
                    # if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
                    #     res = (num1 // num2) + 1
                    # else:
                    #     res = num1 // num2
                    res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
        