class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)-1,-1,-1):
                       
            if count >=1:
                if s[i] != " ":
                    count +=1
                else: 
                    return count
            if count ==0:
                if s[i] == " ":
                    count+= 0
                elif s[i] != " ":
                    count +=1