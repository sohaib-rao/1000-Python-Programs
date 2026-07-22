from datetime import date, timedelta

today = date.today()
expiry_days = timedelta(days=90)
expiry_date = today + expiry_days

print(f"Password set on: {today}")
print(f"Password will expire on: {expiry_date}")