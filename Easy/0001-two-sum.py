class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Dictionary creation
        dicc = {}

        # Look the list while getting the index and number
        for i, num in enumerate (nums):
  
            # Calculate the complement
            mv= target - num

            # Look if compliment exists in diccionary
            if mv in dicc:

                # Return index
                return [dicc[mv], i]

            # Save number and index
            dicc[num] = i

