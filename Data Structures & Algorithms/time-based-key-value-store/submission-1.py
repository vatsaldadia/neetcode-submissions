class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        
        val_list = self.time_map[key]
        left = 0
        right = len(val_list) - 1
        # print(f"{key=}, {timestamp=}, {val_list=}")
        while left <= right:
            mid = left + (right - left) // 2
            mid_time = val_list[mid][0]
            # print(f"\t{left=}, {right=}, {mid=}, {mid_time=}")
            if mid_time == timestamp:
                return val_list[mid][1]
            if mid_time > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return val_list[right][1]