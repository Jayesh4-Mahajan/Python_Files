import string
from time import gmtime, strftime
import datetime
import dateutil
from dateutil.relativedelta import relativedelta

def create_date_range(StartDate,EndDate = (datetime.datetime.now().date()-datetime.timedelta(days=2)),day = -1) :
    date_range = []
    date = datetime.datetime.strptime(StartDate, "%Y-%m-%d").date()
    if type(EndDate) == str:
        EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d").date()
    while date < EndDate:
        if day == -1:
            d1,d2 = date, date + relativedelta(day=31)
        else:
            d1,d2 = date, date + datetime.timedelta(days=day)
        date = d2 + datetime.timedelta(days = 1)
        if d2 > EndDate:
            d2 = EndDate
        date_range.append((str(d1),str(d2)))
    if EndDate != datetime.datetime.strptime(date_range[-1][1], "%Y-%m-%d").date():
        date_range.append((str(d1+datetime.timedelta(days=1)),str(EndDate)))
    return date_range

date_range = create_date_range('2019-02-03','2020-03-15',day=15)
for dates in date_range:
    print(dates[0],dates[1])
