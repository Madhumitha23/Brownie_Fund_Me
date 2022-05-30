
from brownie import FundMe, accounts
from scripts.helpful_scripts import get_accounts

def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    print(account)
    print(fund_me)
    #account = get_accounts()
    entrance_fee =fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.Fund({"from":account, "value":entrance_fee})

def withdraw():
    fund_me=FundMe[-1]
    account = get_accounts()
    
    fund_me.withdraw({"from":account})

def main():
    fund()
    withdraw()
