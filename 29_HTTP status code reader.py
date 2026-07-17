status_code = 404

match status_code:
    case 200:
        print("Success! Data retrieved.")
    case 400:
        print("Bad Request. Check your syntax.")
    case 404:
        print("Not Found. The page does not exist.")
    case 500:
        print("Internal Server Error.")
    case _:
        print(f"Unknown status code: {status_code}")