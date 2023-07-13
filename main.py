class TimeEquality:
    @staticmethod
    def find_time(array):
        max = float("-inf")
        for i in array:
            if i > max:
                max = i

        count = 0
        for j in array:
            if j != max:
                count += max - j

        return count
array = list(map(int, input().split()))
result = TimeEquality()
print(result.find_time(array))