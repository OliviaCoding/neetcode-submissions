class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        pairs = self.time_map[key]
        res = ""
        left, right = 0, len(pairs) - 1

        while left <= right:
            mid = left + (right - left) // 2
            current_time = pairs[mid][1]

            if current_time == timestamp:
                return pairs[mid][0]

            elif current_time < timestamp:
                left = mid + 1
                res = pairs[mid][0]

            else:
                right = mid - 1
        
        return res



        
