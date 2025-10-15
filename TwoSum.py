from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_to_index = {} # Dictionary/hash map to store number and its index, automatically stores the index of the first occurrence of each number.
    
    # Go through the list and check to see if we've seen the complement before
    # Enumerate allows for using both the index and the value of each number in the list.
    for i, num in enumerate(nums):
        complement = target - num # Check to see what the other number needed to reach the desired sum is.
        if complement in num_to_index:
            return [num_to_index[complement], i] #Return the indices of the two numbers that add up to the target.
        num_to_index[num] = i
    
    return []

# Example usage:
nums = [2, 8, 7, 15]
target = 9
print(twoSum(None, nums, target))