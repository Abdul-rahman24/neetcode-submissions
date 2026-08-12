class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1

            if seen[i]>1:
                return True
        return False
        