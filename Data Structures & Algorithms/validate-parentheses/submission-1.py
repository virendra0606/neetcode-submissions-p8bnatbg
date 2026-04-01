class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        if (j+1)/2 !=(j+1)//2 :
            return False
        while i<j:
            if (ord('(')==ord(s[i]) and ord(')')==ord(s[j])) or (ord('[')==ord(s[i]) and ord(']')==ord(s[j])) or (ord('{')==ord(s[i]) and ord('}')==ord(s[j])):
                i+=1
                j-=1
            elif (ord('(')==ord(s[i]) and ord(')')==ord(s[i+1])) or (ord('[')==ord(s[i]) and ord(']')==ord(s[i+1])) or (ord('{')==ord(s[i]) and ord('}')==ord(s[i+1])):
                i+=2
            else:
                return False
        return True

        