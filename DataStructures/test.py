class Runningavg:

    def __init__(self, max_value = float('inf'), min_value = float("-inf")):
        self.runningavg = 0
        self.count = 0 
        self.max_value = max_value
        self.min_value = min_value

    def get_runninAvg(self, num):
        self.runningavg += num
        self.count += 1
        num = max(self.min_value, min(self.max_value, num))
        print(num)

        return self.runningavg / self.count





input = [10,20,30,40,50, -1,10001]
rv = Runningavg(max_value = 10000, min_value = 0)
for i in input:
    print(rv.get_runninAvg(i))
        

