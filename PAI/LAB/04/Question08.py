class Account:
    def __init__(self, account_num, account_bal, security_code):
        self.__account_num = account_num
        self.__account_bal = account_bal
        self.__Security_code = security_code

    def SetAccountNum(self, account_num):
        print("Set the account number: ")
        self.__account_num = account_num

    def setAccountBal(self, account_bal):
        print("Add Amount in this Account: ")
        self.__account_bal += account_bal

    def SetSecurityCode(self, code):
        print("set The Security code of Account: ")
        self.__Security_code = code

    def Get_Account_Num(self):
        return self.__account_num

    def Get_Account_Bal(self):
        return self.__account_bal

    def Get_Security_code(self):
        return self.__Security_code

    def Get_info(self):
        print(f"Account Number: {self.__account_num}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__Security_code}")


account1 = Account(0, 0.0, 0)
account1.setAccountBal(1200)
account1.SetAccountNum(12345)
account1.SetSecurityCode(5432)

account1.Get_info()