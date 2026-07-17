command = ["go", "north"]

match command:
    case ["go", direction]:
        print(f"You start walking {direction}.")
    case ["take", item]:
        print(f"You put the {item} in your inventory.")
    case ["drop", item]:
        print(f"You leave the {item} on the ground.")
    case ["quit" | "exit"]:
        print("Thanks for playing!")
    case _:
        print("I don't understand that command.")