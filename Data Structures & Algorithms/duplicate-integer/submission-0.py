class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set(nums)
        return len(nums) != len(dupes)
