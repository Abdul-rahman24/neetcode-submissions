class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict={}

        for i in nums:
            dict[i]=dict.get(i,0)+1

        l=[]

        for i,j in dict.items():
            l.append((j,i))

        z=sorted(l
        )

        t=[]
        
        while len(t)<k:
            t.append(z.pop()[1])


        return t

        
        