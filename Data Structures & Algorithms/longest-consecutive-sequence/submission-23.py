class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        num=set(nums)
        longest=0
        
        

        for i in num:
            if i-1 not in num:
                current=i
                length=1

                while current+1 in num:
                    current+=1
                    length+=1
                
                longest=max(length,longest)
        return longest
            

        