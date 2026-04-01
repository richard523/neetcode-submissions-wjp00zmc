class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    hashset = set() # Python can define a set like so
    for n in nums: # Create a loop for num in nums
      if n in hashset: # Check existence in hashset at O(1)
        return True # Return True if already exists
      hashset.add(n) # Continue and add element to the set
    return False # Finally return False if our loop exits