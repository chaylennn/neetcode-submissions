class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        best = 0
        i = 0
        j = len(heights) - 1

        while (i < j):
            checking = ((j-i) * min(heights[i], heights[j]))
            if checking > best:
                best = checking
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        

        return best