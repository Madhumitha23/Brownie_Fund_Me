//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
contract FundMe
{
    mapping(address=>uint256) public addressToValue;
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }
    
    function Fund() public payable
    {
        //minimum $50
        //require(getConversionRate(msg.value)>=50*10**18,"You need to spend extra eth!");
        addressToValue[msg.sender]+=msg.value;
        funders.push(msg.sender);
    }
    function getVersion() public view returns (uint256)
    {
        //AggregatorV3Interface PriceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    function getPrice() public view returns (uint256)
    {
        //AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (
            //uint80 roundId,
            ,int256 answer,,,
            //uint256 startedAt,
            //uint256 updatedAt,
            //uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        return uint256(answer * 1000000000000000000);
    }
    // 1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice*ethAmount) / 1000000000000000000;
        return ethAmountInUSD;
        //208517977818000000000
    }

    function getEntranceFee() public view returns (uint256){
        //minimum USD
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision) / price;

    }

    modifier ownerCheck{
        require(owner == msg.sender);
        _;
    }

    function withdraw() payable ownerCheck public{
        
        payable(msg.sender).transfer(address(this).balance);
        for(uint256 funderindex=0;funderindex<funders.length;funderindex++)
        {
            address funder = funders[funderindex];
            addressToValue[funder]=0;
        }
        funders = new address[](0); 
    }

    
}