class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        time = [0] * len(cars)
        for idx in range(len(cars)):
            p = cars[idx][0]
            s = cars[idx][1]
            distance = target - p
            time[idx] = distance / s
        stack = []
        for i in time:
            if stack and stack[-1] >= i:
                continue
            else:
                stack.append(i)
        # print(cars, time, stack, sep='\n')
        return len(stack)