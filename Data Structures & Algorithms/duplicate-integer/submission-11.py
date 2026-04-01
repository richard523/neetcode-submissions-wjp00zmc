class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i, e in enumerate(nums):
            if e in hashset:
                return True
            hashset.add(e)
        return False
