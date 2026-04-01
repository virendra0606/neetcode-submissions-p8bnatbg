class Solution:
    def is_alpha(self,c):
        if "a"<=c<="z" or "A"<=c<="Z" or str(0)<=c<=str(9):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        new_str = s.lower()
        l = 0
        r = len(s)-1
        while l<r:
            if new_str[l]==new_str[r]:
                l+=1
                r-=1
            elif not self.is_alpha(new_str[l]):
                l+=1
            elif not self.is_alpha(new_str[r]):
                r-=1
            else:
                return False
        return True
        