class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        data = {}
        for i in range(len(s)):
            if s[i] in data:
                data[s[i]]+=1
            else:
                data[s[i]]=1
        for i in range(len(t)):
            if t[i] in data:
                if data[t[i]]>0:
                    data[t[i]]-=1
                else:
                    return False
            else:
                return False
        return True
        