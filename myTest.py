from datetime import date, datetime, time, timedelta

dt = datetime.combine(date.today(), time(00, 29)) - timedelta(minutes=22)
print ()