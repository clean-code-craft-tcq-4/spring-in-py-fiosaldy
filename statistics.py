def calculateStats(numbers):
    stat_res = {}
    #Check if list is empty or not 
    if len(numbers) > 0:
        stat_res = {"max" : 0.0, "min" : 0.0, "avg" : 0.0}
        numbers.sort()
        #First element is min and the last is max, after the above sorting
        stat_res["min"] = float(numbers[0])
        stat_res["max"] = float(numbers[-1])
        #Loop through all the numbers to find the average
        for i in numbers:
            stat_res["avg"] += i
        stat_res["avg"] = float(stat_res["avg"]/len(numbers))
    else:
        #Intialising Not a Number (NaN) if array is empty
        stat_res = {"max" : "nan", "min" : "nan", "avg" : "nan"}
    return stat_res

class StatsAlerter():
    #Initialise variables
    def __init__(self, maxT, alerts):
        self.maxThreshold = maxT
        self.emailAlert = alerts[0]
        self.ledAlert = alerts[1]

    def checkAndAlert(self, num_arr):
        #Loop through array and check id max Threshold is exceeded
        for i in num_arr:
            if i > self.maxThreshold:
                self.emailAlert.update()
                self.ledAlert.update()

##Functions defined as class for ease of implementaion of the alert counter 

class EmailAlert():
    #Initialise alert variable for Emails
    def __init__(self):
        self.emailSent = 0
    def update(self):
        #Updating the counter to track Email Alert Frequency
        self.emailSent += 1
        
class LEDAlert():
    #Initialise alert variable for LED
    def __init__(self):
        self.ledGlows = 0
    def update(self):
        #Updating the counter to track the frequency of the LED glowing
        self.ledGlows += 1
        
