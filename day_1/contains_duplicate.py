"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
# First Attempt
class Solution:
    def containsDuplicate(self, nums):
        # second array to check against.
        newArr = []
        # loop over nums.
        for i in nums:
            # check if it is already in newArr
            if i in newArr:
                # if it is return true
                return True
            # if it's not   
            else:
                # add to newArr
                newArr.append(i)
            # if we get to the end and never return true, return false
        return False
# Works but takes to long

# 2nd Attempt
class Solution2:
    def containsDuplicate(self, nums):
        # sort nums first
        nums.sort()
        # loop over nums.
        for i in nums:
            # check if i matches i + 1 
            if nums[i] == nums[i + 1]:
                # if it does return true
                return True
            # if we get to the end and never return true, return false
        return False
# Gotta figure out how to not run off the end of the array in python

"""
Javascript version of attempt 2
var containsDuplicate = function(nums) {
    nums.sort();
    for( i = 0; i < nums.length - 1; i++){
        if(nums[i] == nums[i + 1])
            return true; 
    }
    return false;
};
"""

# 3rd Attempt
class Solution3:
    def containsDuplicate(self, nums):
        # sets can't have duplicates os if it does it will be longer
        if len(set(nums)) < len(nums):
            return True 
        else:
            return False

# 4th Attempt
class Solution4:
    def containsDuplicate(self, nums):
        dic = {}
        for n in nums:
            if n in dic: 
                return True
            else: 
                dic[n] = 1
        return False
