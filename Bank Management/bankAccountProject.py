 import json
import random
import string
from pathlib import Path
class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
             with open (database) as fs:
                 data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def update(cls):
        with open(cls.database,'w') as fs: 
            fs.write(json.dumps(Bank.data))

    # @classmethod
    # def update(cls):
    #     with open(cls.database, 'w') as fs:
    #         json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=4)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar 
        random.shuffle(id)
        return "".join(id)


    def Createaccount(self):
        info = {
            "name": input("Tell your name:-"),
            "age": int(input("tell your age:-")),
            "email": input("tell your email:-"),
            "pin": int(input("tell your pin:-")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0 
        }

        if info['age'] < 18 or len(str(info['pin'])) !=4: 
            print("sorry you can not create your account")
        else:
            print("account has been created successfully ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
        
            Bank.update()

    def depositmoney(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin aswell : "))
        # print(Bank.data)

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if  userdata == False :
            print("sorry no data found ")
        else:
            amount = int(input("How much you want to deposit "))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                # print(userdata) 
                userdata [0]['balance'] += amount
                Bank.update()
                print("Amount deposited successfully ")

    def withdrawmoeny(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin aswell : "))
        # print(Bank.data)
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False :
            print("sorry no data found ")
        else:
            amount = int(input("How much you want to withdrow "))
            if userdata[0] ['balance'] < amount:
                print("sorry you don't have that much noney")
            else:
                # print(userdata)
                userdata[0] ['balance'] -= amount
                Bank.update()
                print("your amount withdraw successfully")


    def showdetails(self):

        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin aswell : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your information are \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
    

    def updateDetails(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("please tell your pin aswell : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")
        else:
            print("you can not change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")


            newdata = {
                "name" : input("Please tell your name or press enter :  "),
                "email" : input("please tell your new email or press enter to skip : "),
                "pin" : input("enter new  pin or press enter to skip : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['name']
            if newdata["pin"] == "":
                newdata["email"] = userdata[0]['name']
            

            newdata["age"] = userdata[0]['age']
            newdata["accountNo."] = userdata[0]['accountNo.']
            newdata["balance"] = userdata[0]['balance']

            if type(newdata['pin']) == str: 
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                 
            Bank.update()
            print("Details updated successfully.")

    def Delete(self):
        accnumber = input("please tell your account number : ")
        pin = int(input("Enter your pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such data exist.")
        else:
            check = input("Press y if actually want to delete data the account or press n")
            if check == 'n':
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.update()


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for Deposititing the money is the bank")
print("Press 3 for Withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 deleting your account")

check = int(input("tell your responcse :-"))

if(check == 1):
    user.Createaccount()
if(check == 2):
    user.depositmoney()
if(check == 3):
    user.withdrawmoeny()
if(check == 4):
    user.showdetails()
if(check == 5):
    user.updateDetails()
if(check == 6):
    user.Delete()