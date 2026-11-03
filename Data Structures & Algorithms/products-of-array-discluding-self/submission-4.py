class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l=[1]*len(nums)
        m=[1]*len(nums)
        n=[1]*len(nums)

        pre=1
        for i in range(len(nums)):
            l[i]=pre
            pre=pre*nums[i]

        suf=1

        for i in range(len(nums)-1,-1,-1):
            m[i]=suf
            suf*=nums[i]

        for i in range(len(nums)):
            n[i]=l[i]*m[i]

        return n
        