class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        i = 0
        if n%2!=0:
            return False
        while i<n:
            if (ord(s[i])==40 and ord(s[i+1])==41) or (ord(s[i])==91 and ord(s[i+1])==93) or (ord(s[i])==123 and ord(s[i+1])==125) :
                i+=2
                
            elif (ord(s[i])==40 and ord(s[n-1])==41) or (ord(s[i])==91 and ord(s[n-1])==93) or (ord(s[i])==123 and ord(s[n-1])==125):
                i+=1
                n-=1
            else:
                return False
        return True
        