class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        t=sorted(s1)

        for i in range(len(s2)-k+1):

            window=s2[i:i+k]

            if sorted(window)==t:
                return True

        return False



        