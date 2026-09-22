class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dict={}

        dup=0

        for i in nums:
            dict[i]=dict.get(i,0)+1
        for j in dict:
            if dict[j]>1:
                dup=j

        return dup
        