# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法

# 示例1：
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2

# 示例2：
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1

# 示例3：
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4 

# 解题思路：
# 使用二分法查找，left = 0；right=len(nums)。每次只需要比较mid 与 target的大小即可。如果mid == tartget，则直接返回mid。如果mid > target, left = mid-1。如果mid < target, right = mid + 1
# 否则，返回right+1

class Solution:
    def searchInsert(self, nums: List[int],target:int)->int:
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return right + 1