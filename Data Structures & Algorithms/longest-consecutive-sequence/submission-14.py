class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0

        for i in s:
            if (i-1) not in s:
                len=1
                while (i+len) in s:
                    len += 1
                res=max(res,len)
        return res
        