from math import floor

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, 0, len(nums) - 1, target)

    def searchHelper(self, nums: List[int], left: int, right: int, target: int) -> int:
        if (left > right):
            return -1
        
        # left = 0
        # right = len(nums) - 1
        mid = left + (right - left) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return self.searchHelper(nums, left, right, target)