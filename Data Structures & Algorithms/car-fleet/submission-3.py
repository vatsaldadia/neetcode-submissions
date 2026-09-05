class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for idx in range(len(cars)):
            p = cars[idx][0]
            s = cars[idx][1]
            distance = target - p
            time = distance / s
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        # print(cars, time, stack, sep='\n')
        return len(stack)