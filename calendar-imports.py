import calendar
print(calendar.calendar(2021))



print(calendar.month(2020, 11))



calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12) #shows the calendar starting on Sunday



print(calendar.weekday(2020, 12, 24)) #outputs the week day number



print(calendar.weekheader(2)) # will output Mo Tu We Th Fr Sa Su (2 characters)



print(calendar.isleap(2020)) #outputs True
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021, outputs number of leap years between 2010 and 2020



c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ") # will output days of week number, 6 0 1 2 3 4 5 (starts on Sunday which is 6)
    
    
    
    c = calendar.Calendar()
for data in c.monthdays2calendar(2020, 12):
    print(data) #outputs the day of the week with the date of the month
    
    
    
    
