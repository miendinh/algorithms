'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# O(n^2)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	for j in range(i+1, len(nums)):
        		if(nums[i] + nums[j]) == target:
        			return [i, j]

       	return None

nums = [2, 7, 11, 15]
target = 9

assert Solution().twoSum(nums, target) == [0, 1]

nums = [ 3, 2, 4 ]
target = 6

assert Solution().twoSum(nums, target) == [1, 2]


# O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
        	if nums[i] in dict:
        		return [dict[nums[i]], i]
        	else:
        		dict[target - nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

assert Solution().twoSum(nums, target) == [0, 1]

nums = [ 3, 2, 4 ]
target = 6

assert Solution().twoSum(nums, target) == [1, 2]