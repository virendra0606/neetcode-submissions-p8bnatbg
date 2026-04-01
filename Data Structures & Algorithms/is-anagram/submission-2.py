class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for a in range(len(t)):
            if t[a] in dict and dict[t[a]]>=1:
                
                dict[t[a]]-=1
            else:
                return False
        return True
        