class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxx=0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                t=prices[j]-prices[i]

                maxx=max(t,maxx)

        return maxx

        