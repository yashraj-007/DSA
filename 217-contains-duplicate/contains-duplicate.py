class Solution(object):
    def containsDuplicate(self, nums):
        sett = set(nums)

        if len(nums) != len(sett):
            return True
        
        return False