class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        res=0

        for i in num:

            if i-1 not in num:
                current=i
                long=1

                while current+1 in num:
                    current+=1
                    long+=1

                res=max(res,long)

        return res
