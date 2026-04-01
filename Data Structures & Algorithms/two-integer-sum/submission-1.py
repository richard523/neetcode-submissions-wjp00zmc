class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #hashmap
        prevMap = {}

        #enumerate tracks index AND value
        #i is index n is value
        for i, n in enumerate(nums):
            #diff also means diff + n = target
            diff = target - n
            if diff in prevMap:
                #check if diff is in hashmap already
                return [prevMap[diff], i]
            #put n in hashmap
            prevMap[n] = i
        