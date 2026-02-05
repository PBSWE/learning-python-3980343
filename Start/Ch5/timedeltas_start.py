#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#
print('='*15)

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
# print(timedelta(days=365, hours=5,minutes=1))

# print today's date
now = datetime.now()
# print('Today is', now)

# print today's date one year from now
# print('In one year, it will be:', now + timedelta(days=365))

# create a timedelta that uses more than one argument
# print('In two weeks and 3 days it will be:', now + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# #print('t:', t)
# s = t.strftime('%A %B %d, %Y')
# #print('s:', s)
# print('One week ago it was', s)

### How many days until April Fools' Day?
today = date.today()
# today = date(today.year, 11, 10) #mock date
fools = date(today.year, 4, 1)
delta = (today - fools).days
#print(delta, "days left to April Fools' Day.")
if fools < today:
  print(f"April Fools' day already went by {(today-fools).days} days ago.")
  fools = fools.replace(year=today.year+1)

time_to_fools = fools-today
print(f"It's just {time_to_fools.days} days until April Fools' Day")