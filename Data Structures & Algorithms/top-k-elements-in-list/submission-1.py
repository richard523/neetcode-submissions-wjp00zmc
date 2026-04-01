from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        sorted_map = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_map[:k]]
