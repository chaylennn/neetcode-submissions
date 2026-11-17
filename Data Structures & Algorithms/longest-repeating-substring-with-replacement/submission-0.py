class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        first = 0
        window = 0

        i = 0
        while i < len(s):
            # add the new letter
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1

            # too many letters to change? shrink from the left
            while (i - first + 1) - max(count.values()) > k:
                count[s[first]] -= 1
                first += 1

            window = max(window, i - first + 1)
            i += 1

        return window