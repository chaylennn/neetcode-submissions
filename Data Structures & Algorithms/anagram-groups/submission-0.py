class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for s in strs:
            if str(sorted(s)) in out:
                out[str(sorted(s))].append(s)
            else:
                out[str(sorted(s))] = [s]
        
        return [lst for lst in out.values()]
        