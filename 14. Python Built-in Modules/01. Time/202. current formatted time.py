import datetime

now = datetime.datetime.now()
formatted_time = now.strftime("%A, %d %B %Y - %I:%M:%S %p")
print(f"Current Date & Time: {formatted_time}")