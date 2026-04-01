class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict = {}

        # for i in range(len(nums)):
        #     rem = target-nums[i]
        #     if rem in dict:
        #         return list(dict[rem]+[i])
        #     else:
        #         dict[nums[i]]=[i]
        data = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in data:
                return list(data[rem]+[i])
            else:
                data[nums[i]] = [i]
        