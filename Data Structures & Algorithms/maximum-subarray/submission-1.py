class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res=nums[0]
        curr=0

        for i in range(len(nums)):
            curr=max(nums[i]+curr,nums[i])

            res=max(curr,res)

        return res


        