class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # inputs
        ## List nums
        ## int target 

        # outputs
        ## List [i, j]

        # rules:
        ## return small index and bigger index

        ### [3,1,5,6] target == 12
        ### [3,1,5,6]

        ## [5,5]
        ## [5,5]
        for i, e in enumerate(nums):
            for j, f in enumerate(nums):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
