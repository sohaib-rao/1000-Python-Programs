point = (3, 4)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print("X-axis")
    case (0, y):
        print("Y-axis")
    case (x, y):
        print("Custom point")