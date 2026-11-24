class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # Create array
        array = set ()
        # Go through numbers
        for num in nums:
            # Validate if the number already exists
            if num in array:
                # Return True
                return True
            # Add number to array
            array.add(num)
        # Return False
        return False
