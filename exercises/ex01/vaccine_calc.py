"""A vaccination calculator."""

__author__ = "730163234"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Pop: int = int(input("Input population size: "))
Doses_admin: int = int(input("Input doses already administered: "))
Doses_day: int = int(input("Input doses per day: "))
Target_Percent: int = int(input("Input target vaccination percent: "))
today: datetime = datetime.today()

Days: int = int(round((((Target_Percent * Pop * 2) / 100) - Doses_admin) / Doses_day))
print(Days)

future: timedelta = timedelta(Days)

VaccineDate: datetime = today + future
print(VaccineDate)

print("We will reach " + str(Target_Percent) + "% vaccination in " + str(Days) + " days, which falls on " + VaccineDate.strftime("%B %d, %Y")) 
