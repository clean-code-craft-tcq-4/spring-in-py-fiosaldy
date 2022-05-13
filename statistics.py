
def calculateStats(numbers):
    stat_res = {}
    if len(numbers) > 0:
        stat_res = {"max" : 0.0, "min" : 0.0, "avg" : 0.0}
        numbers.sort()
        stat_res["min"] = float(numbers[0])
        stat_res["max"] = float(numbers[-1])
        for i in numbers:
            stat_res["avg"] += i
        stat_res["avg"] = float(stat_res["avg"]/len(numbers))
        print(stat_res)
    else:
        stat_res = {"max" : "nan", "max" : "nan", "max" : "nan"}
    return stat_res

class StatsAlerter():
    def __init__(self, maxT, alerts):
        self.maxThreshold = maxT
        self.emailAlert = alerts[0]
        self.ledAlert = alerts[1]

    def checkAndAlert(self, num_arr):
        for i in num_arr:
            if i > self.maxThreshold:
                self.emailAlert.update()
                self.ledAlert.update()

class EmailAlert():
    def __init__(self):
        self.emailSent = 0
    def update(self):
        self.emailSent += 1
        
class LEDAlert():
    def __init__(self):
        self.ledGlows = 0
    def update(self):
        self.ledGlows += 1
        
