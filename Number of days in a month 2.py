def days_in_month(month, year):
  

  days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  
  if month == 2 and is_leap_year(year):
    days_per_month[1] = 29

  return days_per_month[month - 1]

def is_leap_year(year):
 

  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


month = 12
year = 2016

days = days_in_month(month, year)
print(f"There are {days} days in {month}/{year}.")  # Output: There are 29 days in 2/2016.
