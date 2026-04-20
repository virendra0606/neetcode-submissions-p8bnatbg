class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        l = 0 
        count = 0
        maxf = 0
        for i in range(len(s)):
            if s[i] in data:
                data[s[i]]+=1
            else:
                data[s[i]]=1
            maxf = max(maxf,data[s[i]])

            while (i-l+1)-maxf>k:
                data[s[l]]-=1
                l+=1
            count = max(count,i-l+1)
        return count
        