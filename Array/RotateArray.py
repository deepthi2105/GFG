class Solution(object):
    def rotate(self, nums, k):
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        return nums
        
        
