"""
Problem: Two Sum
LeetCode ID: 1
Topics: Array, Hash Table
Problem: Use a dictionary to store previously visited
numbers and their indices
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Dictionary creation
        dicc = {}

        # Look the list while getting the index and number
        for i, num in enumerate (nums):
  
            # Calculate the complement
            mv= target - num

            # Look if complement exists in dictionary
            if mv in dicc:

                # Return index
                return [dicc[mv], i]

            # Save number and index
            dicc[num] = i

