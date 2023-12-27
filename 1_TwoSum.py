# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

##########################################################################################
#Solution 1: Using a Dictionary (Hash Map)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i


#This solution uses a dictionary to store the complement of each number along with its index. While iterating through the array, it checks if the current number's complement is already in the dictionary. If yes, it means we found a pair that adds up to the target.

# Class Definition:
#
# The code defines a class named Solution.
# Method twoSum:
#
# The class contains a method called twoSum.
# It takes two parameters: nums, a list of integers, and target, an integer.
# The return type is specified as a list of integers (List[int]).
# Dictionary num_dict:
#
# Inside the twoSum method, a dictionary num_dict is initialized. This dictionary will be used to store the numbers encountered so far along with their indices.
# For Loop using enumerate:
#
# The code uses a for loop with enumerate(nums) to iterate over each element num in the nums list along with its index i.
# enumerate(nums) returns pairs of indices and elements from the nums list.
# Complement Calculation:
#
# For each num in the loop, the code calculates the complement, which is the difference between the target and the current num. This represents the value that, when added to the current num, would result in the target sum.
# Checking for Complement in Dictionary:
#
# The code checks if the complement is already in the num_dict dictionary. If it is, that means a pair of numbers has been found whose sum is equal to the target.
# If the complement is present in the dictionary, the method immediately returns a list containing the indices of the two numbers that add up to the target: [num_dict[complement], i].
# Updating the Dictionary:
#
# If the complement is not in the dictionary, the current num is added to the dictionary with its index i. This is done to keep track of the numbers encountered so far.
# Completion:
#
# If the loop completes without finding a pair, it means no solution was found, and the method returns an empty list or any other appropriate value.
# This algorithm efficiently finds a pair of indices in the nums list whose corresponding elements add up to the target. The use of a dictionary allows for constant-time lookups, resulting in a time complexity of O(n).

##########################################################################################
#Solution 2: Sorting and Two Pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(sorted_nums) - 1
        
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if current_sum == target:
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


# This solution sorts the array along with their original indices. Then, it uses two pointers (left and right) to find the pair that adds up to the target. If the current sum is less than the target, it moves the left pointer to the right, and if the current sum is greater than the target, it moves the right pointer to the left.
# Both of these solutions have a time complexity of O(n), making them more efficient than the brute-force O(n^2) solution.

# #expl:
# Class Definition:

# The code defines a class named Solution.
# Method twoSum:

# The class contains a method called twoSum.
# It takes two parameters: nums, a list of integers, and target, an integer.
# The return type is specified as a list of integers (List[int]).
# Sorting enumerate(nums):

# Inside the twoSum method, the code uses enumerate(nums) to create pairs of indices and elements from the nums list.
# The sorted function is then used to sort these pairs based on the values of the elements (x[1]), ensuring that the pairs are sorted based on the actual values.
# Initializing Pointers:

# Two pointers, left and right, are initialized. left starts at the beginning of the sorted list, and right starts at the end.
# While Loop:
# The code enters a while loop, which continues as long as the left pointer is less than the right pointer.
# Calculating Current Sum:
# Inside the loop, the code calculates the current sum by adding the values of the elements at the left and right pointers in the sorted list.
# Checking for Target Sum:
# The code checks if the current sum is equal to the target.
# If it is, a pair of indices is found, and the method immediately returns a list containing these indices: [sorted_nums[left][0], sorted_nums[right][0]].
# Adjusting Pointers:
# If the current sum is less than the target, it means we need a larger sum, so the left pointer is moved to the right (increased).
# If the current sum is greater than the target, it means we need a smaller sum, so the right pointer is moved to the left (decreased).
# Completion:
# The while loop continues until the pointers meet (left becomes greater than or equal to right). If no solution is found within the loop, the method implicitly returns None (Python's default return value for functions without an explicit return statement).
# This algorithm uses the two-pointer technique on a sorted list, and the sorting step ensures efficient searching. The time complexity is O(n log n) due to the sorting step. The two-pointer traversal is linear (O(n)), and the dominant term is the sorting step.


# Solution 1: Using a Dictionary (Hash Map)
#
# In this solution, we iterate through the array once, and for each element, we perform constant time operations (dictionary lookups and assignments). The dictionary ensures that the lookups are efficient.
# The overall time complexity is O(n), where n is the length of the input array.
# Solution 2: Sorting and Two Pointers
#
# The sorting step takes O(n log n) time, and the subsequent two-pointer traversal takes O(n) time.
# The dominant term is the sorting step, so the overall time complexity is O(n log n).