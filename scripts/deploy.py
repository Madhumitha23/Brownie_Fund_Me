
from brownie import config,FundMe,network,MockV3Aggregator,accounts
from scripts.helpful_scripts import deploy_mocks
from scripts.helpful_scripts import get_accounts,Local_Blockchain_Environment
def deploy_fund_me():    
    print(f"The active network is {network.show_active()}")
    
    #pass the price feed adress to fundme contract
    if(network.show_active() in Local_Blockchain_Environment):        
       # price_feed_address = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
       deploy_mocks()
      
       price_feed_address = MockV3Aggregator[-1].address
       
    else:       
            
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
    
    print(price_feed_address)
    
    fund_me = FundMe.deploy(price_feed_address,{"from":get_accounts()},publish_source=config["networks"][network.show_active()].get("verify"))
    return fund_me
    
    #print(f"Contracts deployed to {fund_me.getPrice()}")
def main():
    deploy_fund_me()
    