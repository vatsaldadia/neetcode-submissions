class MinStack:

    def __init__(self):
        self.len_min_element_mapper = {0: None}
        self.length = 0
        self.x = []

    def push(self, val: int) -> None:
        self.x.append(val)
        self.length += 1
        if self.length == 1:
            self.len_min_element_mapper[self.length] = val
        else:
            self.len_min_element_mapper[self.length] = min(self.len_min_element_mapper[self.length - 1], val)

    def pop(self) -> None:
        popped = self.x.pop(-1)
        del self.len_min_element_mapper[self.length]
        self.length -= 1

    def top(self) -> int:
        return self.x[-1]

    def getMin(self) -> int:
        return self.len_min_element_mapper[self.length]