class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        left = 0
        right = len(self.store[key]) - 1
        answer = ''
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][0] <= timestamp:
                answer = self.store[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return answer
            

