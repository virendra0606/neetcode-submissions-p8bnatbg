class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dict = {}

        # for i in range(len(numbers)):
        #     rem = target -numbers[i]
        #     if rem in dict:
        #         return [dict[rem],i+1]
            
        #     dict[numbers[i]] = i+1
        # return []
        i = 0
        j = len(numbers)-1
        while i<j:
            Sum = numbers[i] + numbers[j]
            if Sum>target:
                j-=1
            elif Sum<target:
                i+=1
            elif Sum==target:
                return [i+1,j+1]
            else:
                return []
        