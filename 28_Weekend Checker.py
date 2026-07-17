day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend! Time to relax.")
    case "Monday":
        print("Ugh, Monday. Back to work.")
    case "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a regular workday.")
    case _:
        print("That is not a valid day.")