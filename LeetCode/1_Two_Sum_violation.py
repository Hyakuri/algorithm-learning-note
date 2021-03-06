#leetcode
#No.1 Two Sum
#暴力破解法 -> O(n**2)
"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    first_index = j
                    second_index = i
        result = []
        result.append(first_index)
        result.append(second_index)
        return result