import os

# კლასი მომხმარებლის მონაცემებისთვის
class User:
    def __init__(self, username, pin, balance=0):
        self.username = username  # მომხმარებლის სახელი
        self.__pin = pin  # PIN კოდი (ინკაფსულაცია)
        self.balance = balance  # ბალანსი

    # PIN კოდის შემოწმება ავტორიზაციისთვის
    def check_pin(self, pin):
        return self.__pin == pin

    # PIN-ის მიღება (მხოლოდ შიდა გამოყენებისთვის)
    def get_pin(self):
        return self.__pin

    # თანხის შეტანა ანგარიშზე
    def deposit(self, amount):
        self.balance += amount
        return self.balance    

    # თანხის გატანა ანგარიშიდან
    def withdraw(self, amount):
        if amount > self.balance:
            return "არასაკმარისი თანხა!"
        self.balance -= amount
        return self.balance

    # ბალანსის დაბრუნება
    def get_balance(self):
        return self.balance

# ბანკომატის კლასი
class ATM:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename  # ფაილის სახელი, სადაც ინახება მომხმარებლების მონაცემები
        self.users = self.load_users()  # მონაცემების ჩატვირთვა ფაილიდან
    
    # ფაილიდან მომხმარებლების ჩატვირთვა
    def load_users(self):
        users = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    username, pin, balance = line.strip().split(",")
                    users[username] = User(username, pin, float(balance))  
        return users

    # მომხმარებლების მონაცემების შენახვა ფაილში
    def save_users(self):
        with open(self.filename, "w") as file:
            for user in self.users.values():
                file.write(f"{user.username},{user.get_pin()},{user.balance}\n")  # get_pin() ვიყენებთ

    # მომხმარებლის ავთენტიფიკაცია (PIN-ის გადამოწმება)
    def authenticate_user(self, username, pin):
        if username in self.users and self.users[username].check_pin(pin):
            return self.users[username]
        return None

    def create_account(self, username, pin):
        if username in self.users:
            return "მომხმარებელი უკვე არსებობს!"
        self.users[username] = User(username, pin)
        self.save_users()
        return "ანგარიში წარმატებით შეიქმნა!"

    # ბანკომატის მთავარი მენიუ და ოპერაციების შესრულება
    def run(self):
        print("\n Welcome to the ATM ")
        while True:
            choice = input("\n[1] შესვლა [2] ახალი ანგარიში [3] გასვლა: ")
            if choice == "1":
                # ავტორიზაცია
                username = input("მომხმარებლის სახელი: ")
                pin = input("PIN კოდი: ")
                user = self.authenticate_user(username, pin)
                if user:
                    print("ავტორიზაცია წარმატებულია!\n")
                    while True:
                        # მომხმარებლის მენიუ
                        action = input("[1] ბალანსი [2] შეტანა [3] გატანა [4] გამოსვლა: ")
                        if action == "1":
                            print(f"თქვენი ბალანსია: {user.get_balance()}$")
                        elif action == "2":
                            amount = float(input("შეიყვანეთ თანხა: "))
                            print(f"ახალი ბალანსი: {user.deposit(amount)}$")
                            self.save_users()
                        elif action == "3":
                            amount = float(input("გატანის თანხა: "))
                            result = user.withdraw(amount)
                            print(result if isinstance(result, str) else f"ახალი ბალანსი: {result}$")
                            self.save_users()
                        elif action == "4":
                            break  # გამოსვლა მენიუდან
                else:
                    print("არასწორი მონაცემები!")
            elif choice == "2":
                # ახალი ანგარიშის რეგისტრაცია
                username = input("მომხმარებლის სახელი: ")
                pin = input("PIN კოდი: ")
                print(self.create_account(username, pin))
            elif choice == "3":
                print("გმადლობთ, რომ გამოიყენეთ ჩვენი ბანკომატი!")
                break  # ბანკომატიდან გამოსვლა
            else:
                print("არასწორი არჩევანი!")

# პროგრამის გაშვება
if __name__ == "__main__":
    atm = ATM()
    atm.run()