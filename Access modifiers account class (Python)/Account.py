import datetime

class Account:
    _accountNumber = "00378657"
    _openingDate = datetime.datetime.now()
    _currentBalance = 10000
    _interestRate = 2

    #See your account number on todays date
    def GetAccountNumber():
        print("Your account number is: {_accountNumber} at {_openingDate}.")
        print("________________________________________________________________________________")
        Program.Menu()

    #Tells your balance
    #Then asks if you want to make a payment, if 'yes' you choose one, if 'not' you can choose to set up a mortgage amount
    #Otherwise you go back to the menu
    def GetCurrentBalance():
        print("________________________________________________________________________________")
        print("Yoour current balance is: {_currentBalance}")
        answer = input("Do you want to make a payment?")

        if answer == "yes" or answer == "Yes":
            #go to SetPaymentType()
            if answer == "no" or answer == "No":
                userInput = input("Do you want to take out a mortgage?")
            if answer == "yes" or answer == "Yes":
                #go to GetEndDate() then SetEndDate and return
        print("Ok, taking you back to the main menu")
        print("________________________________________________________________________________")
        Menu();
