class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        total_hours = r

        while l<=r:
            mid = (l+r)//2
            hour = 0
            for i in piles:
                hour+= math.ceil(float(i) / mid)

            if hour <= h:
                total_hours = mid
                r = mid - 1
            else:
                l = mid + 1
        return total_hours

        