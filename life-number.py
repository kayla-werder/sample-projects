def digit_of_life(date):
    total = 0
    for num in date:
        total += int(num)
        
        #we have to check for months that are 10, 11, and 12
        if total > 9:
            total = total % 10 + total // 10
    
    print("Life number: " + str(total))
    

user_date = input("Enter your birthday in format (YYYYMMDD):  ")
test = digit_of_life(user_date)