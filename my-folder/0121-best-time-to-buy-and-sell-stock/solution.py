class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        best_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            best = max(best, profit)

        return best
        # sortedprices = sorted(prices)
        # tobuyin = sortedprices[0]
        # best = 0
        # print(tobuyin)
        # ans = 0

        # for i, num in enumerate(prices):
        #     storebuyloc = 0
        #     if tobuyin == prices[i]:
        #         storebuyloc = i
            
            
        #     elif i > storebuyloc:
        #         best = max(best, prices[i])
        #         print(best)

        #     if best == num:
        #         ans = i+1
        #     elif len(prices)-1 < storebuyloc:
        #         ans = 0
            
        # return ans
            










                # storeotherdays = [prices[i]]
                # storeotherdays.sort()
                # storemaxday = storeotherdays[0]




            
            
                
        
