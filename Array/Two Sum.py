'''
Docstring for Array.Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

'''


nums = [3,4,5,6]
target = 7
def twoSum(nums, target):
    num_map = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[nums[i]] = i
    
    return []


def twoSum2(nums, target):
    left, right = 0, len(nums) - 1
    nums_indexed = list(enumerate(nums))
    nums_indexed.sort(key=lambda x: x[1])
    
    while left < right:
        current_sum = nums_indexed[left][1] + nums_indexed[right][1]
        
        if current_sum == target:
            return sorted([nums_indexed[left][0], nums_indexed[right][0]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

print(twoSum(nums, target))
print(twoSum2(nums, target))