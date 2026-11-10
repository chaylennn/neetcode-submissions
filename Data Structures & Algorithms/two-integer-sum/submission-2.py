class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = sorted(nums)
        i = 0
        j = len(num) - 1

        while num[i] + num[j] != target:
            if num[i] + num[j] < target:
                i += 1
            else:
                j -= 1
        
        val1 = num[i]
        val2 = num[j]

        first = nums.index(val1)
        second = nums.index(val2, first + 1) if val1 == val2 else nums.index(val2)

        return sorted([first, second])