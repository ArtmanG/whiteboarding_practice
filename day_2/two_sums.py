"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
# pass 1
class Solution:
    def twoSum(self, nums, target):
        # make a cache {}
        cache = {}
        # make an index pointer 
        index = 0
        # loop through
        for i in nums:
            # make a difference value
            diff = target - i
            # if the target - x = difference and diff is in cache (bingo that's it)
            if diff in cache:
                # return (index, cache[difference]
                return(index, cache[diff])
            # else add x to cache (cache[i] = index)
            cache[i] = index
            # increment index
            index += 1

