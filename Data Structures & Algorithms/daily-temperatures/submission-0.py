class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                popped = stack.pop(-1)
                result[popped] = idx - popped
            stack.append(idx)
            # print(f"{idx=}, {temperatures[idx]=}, {stack=}, {result=}")
        return result