class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        k=0
        for i in range(len(nums)+1):

            k+=i

        t=0

        for i in nums:
            t+=i

        missing=k-t

        return missing
        