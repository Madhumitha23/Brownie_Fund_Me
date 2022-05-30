from brownie import accounts,network,config,MockV3Aggregator
from web3 import Web3
Decimals = 18
Starting_Value=2
Forked_Local_Environment = ["mainnet-fork-dev"]
Local_Blockchain_Environment = ["development","ganache-local"]
def get_accounts():
    
    if(network.show_active() in Local_Blockchain_Environment or network.show_active() in Forked_Local_Environment):
        return accounts[0]
    else:        
        return accounts.add(config["wallets"]["from_key"])
        

def deploy_mocks():
    print("Deploying mocks...")
    if len(MockV3Aggregator)<=0:
       #MockV3Aggregator.deploy(Decimals,Web3.toWei(Starting_Value,"ether"),{"from":get_accounts()})     
       MockV3Aggregator.deploy(Decimals,Starting_Value,{"from":get_accounts()})     
    print("Deployed")