class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n= 0
        idx = 0
        for i in range(len(s)):
            for j in range(idx, len(t)):
                if s[i] == t[j]:
                    n +=1
                    idx = j+1
                    break
        return n==len(s)


        