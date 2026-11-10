class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        out = {}
        for n in nums:
            if n in out:
                out[n] += 1
            else:
                out[n] = 1
        
        vals = sorted(out.values(), reverse=True)   # changed
        max_nums = (vals[:k])                    # changed
        
        out_lst = []

        for key, value in out.items():
            if value in max_nums:
                out_lst.append(key)
        
        return out_lst