class Solution:
    def is_alphanumeric(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        start = 0
        end = len(s)-1

        while start<end:
            while start<end and not self.is_alphanumeric(s[start]):
                start+=1
            while start<end and not self.is_alphanumeric(s[end]):
                end-=1
            if s[start]!=s[end]:
                return False
            
            start+=1
            end-=1
        return True
                 
        