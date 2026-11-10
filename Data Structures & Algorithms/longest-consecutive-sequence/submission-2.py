class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        out = {}

        for i in nums:
            if i in out:
                out[i] += 1
            else:
                out[i] = 1
        
        n = sorted(set(out.keys()))
        longest = []
        temp = 1
        for i in range(len(n)-1):
            if (n[i] + 1 == n[i+1]):
                temp += 1
            else:
                longest.append(temp)
                temp = 1
        longest.append(temp)
        return max(longest) 

        