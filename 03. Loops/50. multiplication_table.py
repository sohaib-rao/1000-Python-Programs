from colorama import Fore

for i in range(1,11):
    print()
    print(Fore.GREEN + "Table of",i)
    for j in range(1,11):
        print(Fore.LIGHTBLUE_EX + f"{i} X {j} = {i * j}")
    