

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        most likely hash
        hash = {}
        
        { index : addend }
        
        input
            nums = [0,1,2,3]
            target = 5
        output:
            2 indeces
            2, 3  (if this is the indicated)
            
            return [2,3]
            
        for 
        
        nums_hash = {}
        
        for i, e in enumerate(nums):
            nums_hash[i] = e
        
        for i, e in enumerate(nums):
            if e + nums_hash[i] == target:
                return [i, nums_hash[i].value()]
        """
        
        nums_hash = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_hash:
                return [nums_hash[complement], i]
            nums_hash[num] = i
        return []