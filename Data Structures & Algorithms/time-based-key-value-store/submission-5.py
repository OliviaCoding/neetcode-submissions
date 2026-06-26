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

        for i in range(len(pairs)):
            if pairs[i][1] == timestamp:
                return pairs[i][0]

            if pairs[i][1] < timestamp:
                res = pairs[i][0]
        
        return res



        
