from datetime import timedelta
from datetime import date
from datetime import datetime

#dt = datetime(2020, 11, 4, 14, 53, 0)

#print(datetime.strptime("2020/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
#print(dt.strftime("%y/%B/%d %H:%M:%S"))

delta = timedelta(weeks=1, days=7, hours=11)
print(delta*2)

input("press x:")
