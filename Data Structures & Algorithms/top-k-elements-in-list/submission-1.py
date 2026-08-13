class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict={}

        for num in nums:
            dict[num]=dict.get(num,0)+1

        result=[]

        for i in range(k):
            maxn=None
            maxc=0

            for j in dict:
                if dict[j]>maxc:
                    maxc=dict[j]
                    maxn=j

            result.append(maxn)
            del dict[maxn]

        return result
                
                    

        