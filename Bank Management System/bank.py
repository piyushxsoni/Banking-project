import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load data safely from JSON
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        print(f"An error occurred while loading data: {err}")
        data = []

    @classmethod
    def update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def __accountgenerate():
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=4)
        spchar = random.choice("!@#$%^&*")
        acc_id = alpha + num + [spchar]
        random.shuffle(acc_id)
        return "".join(acc_id)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return {"status": False, "msg": "Sorry, you cannot create an account."}

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.__accountgenerate(),
            "balance": 0
        }
        Bank.data.append(info)
        Bank.update()
        return {"status": True, "msg": "Account created successfully!", "account": info}

    def deposit_money(self, acc_no, pin, amount):
        user = next((u for u in Bank.data if u['accountNo'] == acc_no and u['pin'] == pin), None)
        if not user:
            return {"status": False, "msg": "Account not found!"}

        if amount <= 0 or amount > 10000:
            return {"status": False, "msg": "Deposit amount must be between 1 and 10000."}

        user['balance'] += amount
        Bank.update()
        return {"status": True, "msg": f"Deposited ₹{amount} successfully!"}

    def withdraw_money(self, acc_no, pin, amount):
        user = next((u for u in Bank.data if u['accountNo'] == acc_no and u['pin'] == pin), None)
        if not user:
            return {"status": False, "msg": "Account not found!"}

        if user['balance'] < amount:
            return {"status": False, "msg": "Insufficient balance."}

        user['balance'] -= amount
        Bank.update()
        return {"status": True, "msg": f"Withdrew ₹{amount} successfully!"}

    def show_details(self, acc_no, pin):
        user = next((u for u in Bank.data if u['accountNo'] == acc_no and u['pin'] == pin), None)
        if not user:
            return {"status": False, "msg": "Account not found!"}
        return {"status": True, "data": user}

    def update_details(self, acc_no, pin, name=None, email=None, new_pin=None):
        user = next((u for u in Bank.data if u['accountNo'] == acc_no and u['pin'] == pin), None)
        if not user:
            return {"status": False, "msg": "No such user found."}

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            user['pin'] = int(new_pin)

        Bank.update()
        return {"status": True, "msg": "Details updated successfully."}

    def delete_account(self, acc_no, pin):
        user = next((u for u in Bank.data if u['accountNo'] == acc_no and u['pin'] == pin), None)
        if not user:
            return {"status": False, "msg": "Account not found!"}

        Bank.data.remove(user)
        Bank.update()
        return {"status": True, "msg": "Account deleted successfully."}
