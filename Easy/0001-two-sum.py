
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Create an empty dictionary to store visited numbers and their indices
        dicc = {}

        # Go through the list while getting the index and number
        for i, num in enumerate (nums):
  
            # Calculate the complement needed to reach the target
            mv= target - num

            # Check if the complement exists in the dictionary
            if mv in dicc:

                # Return indices of the two numbers that add up to the target
                return [dicc[mv], i]

            # Save number and index
            dicc[num] = i

