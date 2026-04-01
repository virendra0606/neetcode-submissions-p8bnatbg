class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        val = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in val:
                val.remove(s[l])
                l+=1
            val.add(s[i])
            res = max(res,i-l+1)
        return res