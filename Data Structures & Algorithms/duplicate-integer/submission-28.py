class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}

        for num in nums:
            if num in table:
                return True
            else:
                table[num] = True
        return False