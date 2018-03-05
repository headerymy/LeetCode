class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        if nums[low]<nums[high]:
            return nums[low]
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[high]:
                low = mid+1
            else: high = mid
        return nums[low]