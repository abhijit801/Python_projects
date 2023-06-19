class Atm:
    def __init__(self):
        self._pin = ''
        self._balance = 0
        self.menu()

    def menu(self):
        user = input("""Hi, how can I assist you?
        1. Press 1 to create PIN
        2. Press 2 to change PIN 
        3. Press 3 to check balance 
        4. Press 4 to withdraw
        Press any other key to exit.
        """)

        if user == '1':
            self.create_pin()
        elif user == '2':
            self.change_pin()
        elif user == '3':
            self.check_balance()
        elif user == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your PIN: ")
        self._pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self._balance = user_balance
        print("PIN created successfully")

        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self._pin:
            new_pin = input("Enter your new PIN: ")
            self._pin = new_pin
            print("PIN change successful.")
        else:
            print("Enter correct PIN.")

        self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self._pin:
            print("Your balance is", self._balance)
        else:
            print("PIN is incorrect")

        self.menu()

    def withdraw(self):
        user_pin = input("Enter your PIN: ")

        if user_pin == self._pin:
            amount = int(input("Enter the amount: "))
            if amount <= self._balance:
                self._balance -= amount

                print(f"Withdrawal of {amount} Rs is successful.")
                print("Your remaining balance is", self._balance)
            else:
                print("Insufficient balance.")
                self.menu()
        else:
            print("PIN is incorrect.")

        exit()


obj = Atm()
