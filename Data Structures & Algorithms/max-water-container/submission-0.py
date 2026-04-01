class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        current =0
        
        while l<r:
            max_water = min(heights[l],heights[r])*(r-l)
            current = max(current,max_water)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return current
            
        