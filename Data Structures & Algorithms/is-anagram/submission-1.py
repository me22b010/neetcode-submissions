class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     a = True
        #     for i in range (len(t)):
        #         if s[i] in t:
        #             i+=1
        #         else:
        #             a = False
        #     return a            
        # else:
        #     return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False