
from brownie import accounts,network,exceptions
from eth_account import Account
from scripts.helpful_scripts import get_accounts,Local_Blockchain_Environment
from scripts.deploy import deploy_fund_me
import pytest 


def test_fund_and_withdraw():
    account = get_accounts()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx1 = fund_me.Fund({"from":account,"value":entrance_fee})
    tx1.wait(1)
    
    assert fund_me.addressToValue(account.address)==entrance_fee

    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToValue(account.address)==0

def test_only_owner_can_withdraw():
    if(network.show_active() not in Local_Blockchain_Environment):
        pytest.skip("only for local testing")
    account = get_accounts()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})
    