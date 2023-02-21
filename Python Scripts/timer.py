class Timer:
    def __init__(self, h, m ,s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __str__(self):
        return (str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

    def next_second(self):
        if(self.seconds == 59 and self.minutes == 59 and self.hours == 23):
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        
        elif(self.seconds == 59 and self.minutes == 59):
            self.seconds = 0
            self.minutes = 0
            self.hours += 1 
        
        elif(self.seconds == 59):
            self.seconds = 0
            self.minutes += 1
        
        else:
            self.seconds +=1
            
        

    def prev_second(self):
        if(self.seconds == 0 and self.minutes == 0 and self.hours == 0):
            self.seconds = 59
            self.minutes = 59
            self.hours = 23
        
        elif(self.seconds == 0 and self.minutes == 0):
            self.seconds = 59
            self.minutes = 59
            self.hours -= 1
        
        elif(self.seconds == 0):
            self.seconds = 59
            self.minutes -= 1
        
        else:
            self.seconds -=1


timer = Timer(1, 0, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
