'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

-----------------------------------------------------------------------------------------

Approach 1: Using Set + Loop (Optimal & Interview-Preferred)
🔸 Intuition

A set stores only unique elements

While traversing the array:

If an element is already in the set, it means we’ve seen it before → duplicate found

Otherwise, store it in the set

🔸 Algorithm

Create an empty set seen

Traverse the array

For each element:

If it exists in seen, return True

Else, add it to seen

If loop finishes, return False
🔸 Dry Run
Input:
nums = [1, 2, 3, 1]

Step	num	seen set	num in seen?	Result
1	1	{}	No	add → {1}
2	2	{1}	No	add → {1,2}
3	3	{1,2}	No	add → {1,2,3}
4	1	{1,2,3}	Yes	return True
🔸 Time & Space Complexity

Time: O(n)
Space: O(n) (extra set)

'''
b = [1, 2, 3, 1]
def containsDuplicate(nums):
    a =  set()
    for i in nums:
        if i in a:
            return True
        a.add(i)
    return False

'''
✅ Approach 2: Length Comparison Using Set (Clean & Short)
🔸 Intuition

A set removes duplicates

If the length of:

original list ≠ set of list
→ duplicates exist

🔸 Algorithm

Convert list to set

Compare lengths

If unequal → duplicate exists

🔸 Dry Run

Input:

nums = [1, 2, 3, 1]

len(nums)      = 4
len(set(nums)) = 3


Since:

4 != 3 → True

🔸 Time & Space Complexity

Time: O(n)

Space: O(n)
'''

def secondSolution(nums):
    return len(nums) != len(set(nums))


print(containsDuplicate(b))
print(secondSolution(b))