response = "YES"
cleaned_response = response.strip().lower()
if cleaned_response == "yes":
    print("Confirmed")
else:
    print("Declined")