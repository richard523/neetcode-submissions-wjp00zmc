class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()

        # 0 1 1
        # 1 1 2
        # 2 1 3
        # 3 2 3  true

        # 0 1 1
        # 1 1 2
        # 2 1 3
        # 3 1 4 false
        for i, e in enumerate(nums):
            if e in tracker:
                return True
            tracker.add(e)
        return False