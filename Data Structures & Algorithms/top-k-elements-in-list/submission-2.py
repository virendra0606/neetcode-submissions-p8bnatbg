class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            if nums[i] in data:
                data[nums[i]]+=1
            else:
                data[nums[i]]=1
        sort = sorted(data.items(), key=lambda x:x[1] , reverse = True)
        output = [item[0] for item in sort[:k]]
        return output
        