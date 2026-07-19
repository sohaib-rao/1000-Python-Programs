class PrepaidSim:
    def __init__(self, phone_number, balance):
        self.phone_number = phone_number
        self.balance = balance
        print(f"SIM activated: {self.phone_number} | Balance: Rs {self.balance}")

    def load_card(self, amount):
        self.balance += amount
        print(f"Load successful. New balance: Rs {self.balance}")

    def make_call(self, minutes):
        call_cost = minutes * 3
        if self.balance >= call_cost:
            self.balance -= call_cost
            print(f"Call connected for {minutes} mins. Deducted: Rs {call_cost}")
        else:
            print(f"Call failed! Need Rs {call_cost}, but you have Rs {self.balance}")

    def check_balance(self):
        print(f"Remaining balance: Rs {self.balance}")

my_sim = PrepaidSim("0300-1234567", 20)

my_sim.make_call(5)
my_sim.make_call(10)
my_sim.load_card(50)
my_sim.make_call(10)
my_sim.check_balance()