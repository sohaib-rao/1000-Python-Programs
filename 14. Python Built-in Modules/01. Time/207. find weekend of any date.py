import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")
date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")

weekday = date_obj.strftime("%A")
print(f"The day on {date_input} was {weekday}.")