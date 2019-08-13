#Test 1 Coding portion - classes and objects
# zhou, Christina
#CSC 231 001
# spring 2019

from BankAccount import *
import statistics

def initialize():
    """initalizes the list for total accounts. reads in a file and processes it
        :returns a list of Bank Account objects"""
    filename = "accounts.csv"
    fileIn = open(filename, "r+")
    totalAccounts = []
    next(fileIn)
    for line in fileIn.readlines():
        line = line.rstrip("\n")
        account = line.split(",")

        acct_num = int(account[0])
        first_name = account[1]
        last_name = account[2]
        balance = float(account[3])

        acc = BankAccount(acct_num, first_name, last_name, balance)

        if acc not in totalAccounts:
            totalAccounts.append(acc)


    return totalAccounts

def printAccounts( totalAccounts):
    """prints the total accounts"""
    for acc in totalAccounts:
        print(acc)


def averageBalace(totalAccounts):
    """calculates the average balance amongst all the accounts"""
    tBalance = 0
    numLines = 0
    for account in totalAccounts:
        tBalance += account.getBalance()
        numLines+=1
    avgBalance = tBalance / numLines
    print( "average balance: " +  str(avgBalance))


def biggestBalance( totalAccounts):
    """calculates the biggest balance amongst all the accounts"""
    balances = []
    for account in totalAccounts:
        balances.append(float(account.getBalance()))

    balances.sort()
    bigB = balances.pop()


    for account in totalAccounts:
        if bigB == account.getBalance():
            print( "biggest balance: " , account)
            break

def medianBalance( totalAccounts):
    """calculates the median balance amongst all the accounts"""
    balances = []
    for account in totalAccounts:
        balances.append(float(account.getBalance()))
        median = statistics.median(balances)

    print( "median balance: " + str(median))

def avgWInterest(totalAccounts):
    """calculates the average balance amongst all the accounts after interest"""
    tBalance = 0
    numLines = 0
    for account in totalAccounts:
        tBalance += account.calculate_interest()
        numLines += 1
    avgWInterest = tBalance / numLines
    print( "average balance with interest: " + str(avgWInterest))


def main():

    totalAccounts = initialize()

    averageBalace(totalAccounts)
    biggestBalance(totalAccounts)
    medianBalance(totalAccounts)
    avgWInterest(totalAccounts)


main()