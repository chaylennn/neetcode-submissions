class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        window = 1
        d = set()

        last = 0
        i = 0
        while i < len(s):
            if s[i] in d:
                d.remove(s[last])
                last += 1
            else:
                d.add(s[i])
                i += 1
                if len(d) > window:
                    window = len(d)

        return window