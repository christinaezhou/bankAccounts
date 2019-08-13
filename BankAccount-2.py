#Test 1 Coding portion - classes and objects
# zhou, Christina
#CSC 231 001
# spring 2019

class BankAccount(object):
    def __init__(self, acct_num, first_name, last_name, balance ):
        self.acct_num = acct_num
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def getAccNum(self):
        return self.acct_num

    def setAccNum(self, acct_num):
        self.acct_num = acct_num

    def getFName(self):
        return self.first_name

    def setFName(self, first_name):
        self.first_name = first_name

    def getLname(self):
        return self.last_name

    def setLname(self, last_name):
        self.last_name = last_name

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def __str__(self):

        return str(self.getAccNum()) + ", " + self.getLname() + "," + self.getFName() + ": $" + str(self.getBalance())

    def __eq__(self, other):

        if (self.getAccNum() == other.getAccNum()):
            print("warning! account number already exisits: " +  str(self.getAccNum()))
            return True
        else:
            return False

    def deposit(self, amt):
        """adds the amt to the account balance"""
        newBalance = self.getBalance() + amt
        return newBalance
    def withdraw(self, amt):
        """subtracts the amount from the account balance"""
        newBalance = self.getBalance() - amt
        return newBalance
    def calculate_interest(self):
        """returns the amount of interest earned on the account balance"""
        interest = 0.015 * self.balance + self.balance
        return interest