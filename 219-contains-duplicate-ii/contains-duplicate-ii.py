class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        l = 0
        for i in range(len(nums)):
            if i - l > k:
                window.discard(nums[l])
                l += 1
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False
