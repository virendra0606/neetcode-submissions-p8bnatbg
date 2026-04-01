class Solution:
    def alphaNumeric(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1

        while i<j:
            
            while i<j and not self.alphaNumeric(s[i]):
                i+=1
            while i<j and not self.alphaNumeric(s[j]):
                print(s[j])
                j-=1
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
        