class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for i in nums:
            data[i] = data.get(i,0) +1
            
        sorted_data = sorted(data.items(),key = lambda x:x[1],reverse=True)
        output = [item[0] for item in sorted_data[:k]]
        return output        