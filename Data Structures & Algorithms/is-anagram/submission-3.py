class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict = {}
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     if s[i] in dict:
        #         dict[s[i]]+=1
        #     else:
        #         dict[s[i]]=1
        # for a in range(len(t)):
        #     if t[a] in dict and dict[t[a]]>=1:
                
        #         dict[t[a]]-=1
        #     else:
        #         return False
        # return True
        data = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in data:
                data[s[i]]+=1
            else:
                data[s[i]] = 1
        for j in range(len(t)):
            if t[j] in data and data[t[j]]>=1:
                data[t[j]]-=1
            else:
                return False
        return True
        