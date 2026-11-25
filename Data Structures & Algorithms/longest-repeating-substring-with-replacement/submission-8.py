class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        res=0
        xurr=0
        dict={}

        for right in range(len(s)):
            dict[s[right]]=dict.get(s[right],0)+1

            xurr=max(xurr,dict[s[right]])

            while (right-left+1)-xurr>k:
                dict[s[left]]-=1
                left+=1

            res=max(res,right-left+1)

        return res


        