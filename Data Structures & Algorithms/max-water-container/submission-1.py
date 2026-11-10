class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        areas = set()
        i = 0
        j = len(heights) - 1

        while (i < j):
            areas.add((j-i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        

        return max(areas)