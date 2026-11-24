class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res=0

        for i in range(len(prices)):
            for j in range(i,len(prices)):

                if prices[i]>prices[j]:
                    break
                curr=prices[j]-prices[i]

                res=max(res,curr)

        return res

            

        