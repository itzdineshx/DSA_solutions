class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Stores Visited Values
        for i in nums:
            if i in seen:
                return True # Already in seen? -> Return True
            seen.add(i) # New element? -> Add it
        return False # Nothing Found? -> False