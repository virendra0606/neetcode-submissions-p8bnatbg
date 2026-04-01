class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = set(nums)
        longest = 0
        for item in nums:
            if (item-1) not in result:
                length = 1
                while (item+length) in result:
                    length+=1
                longest = max(longest,length)
        return longest
        