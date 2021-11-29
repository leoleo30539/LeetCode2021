int maxProfit(int* prices, int pricesSize){
    if(pricesSize == 1)
        return 0;
    
    int profit = 0;
    int buy = 30001;
    for(int i=0; i<pricesSize; i++){
        if(prices[i] > buy)
            profit += prices[i] - buy;
        buy = prices[i];
    }
    return profit;
}