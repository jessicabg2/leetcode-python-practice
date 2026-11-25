class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        #  Create an empty set to store previously visited numbers
        array = set ()
        # Go through numbers in the set
        for num in nums:
            # Validate if the number already exists
            if num in array:
                # Return True if the number is found
                return True
            # Add the number to set for future checks
            array.add(num)
        # Return False if no duplicates are found after checking all numbers
        return False
