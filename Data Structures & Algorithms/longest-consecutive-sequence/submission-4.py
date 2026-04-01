class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = set(nums)
        count = 0
        for num in nums2:
            if (num-1) not in nums2:
                length =1 
                while (num+length) in nums2:
                    length+=1
                count = max(count,length)
        return count

        