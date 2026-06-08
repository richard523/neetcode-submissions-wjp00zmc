class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        input is [1,2,3,1]
        output is true
        
        int arr: nums
        
        first thought:
            set
                you cannot have more than 1 unique item
        
        """
        
        unique_ints = set()
        
        for i, e in enumerate(nums):
            if e in unique_ints:
                return True
            else:
                unique_ints.add(e)
        return False
            
        