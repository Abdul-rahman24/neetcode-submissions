class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l=[1]*len(nums)
        

        pre=1
        for i in range(len(nums)):
            l[i]=pre
            pre=pre*nums[i]

        suf=1

        for i in range(len(nums)-1,-1,-1):
            l[i]*=suf
            suf*=nums[i]

        

        return l
        