class WeekDayError(Exception):
    pass
	

class Weeker:
    
    __dayOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__stat = self.__dayOfWeek.index(day)
        except:
            raise WeekDayError

    def __str__(self):
        return self.__dayOfWeek[self.__stat]

    def add_days(self, n):
        self.__stat = (self.__stat + n) % 7

    def subtract_days(self, n):
        self.__stat = (self.__stat - n) % 7



try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
