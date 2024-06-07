import datetime
t=datetime.datetime.now().date()
print(t)
days_to_add=int(input("enter the number of days to add:"))
new_date=t+datetime.timedelta(days_to_add)
print(new_date)