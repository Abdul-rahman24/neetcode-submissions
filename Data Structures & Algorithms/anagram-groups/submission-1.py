class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        dict={}

        for i in strs:
            n="".join(sorted(i))
            
            dict[n]=dict.get(n,[])+[i]

        return list(dict.values())


        