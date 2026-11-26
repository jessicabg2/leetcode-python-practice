class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        # 1. Create an empty dictionary
        dicc = {}

        # 2. Iterate through the list, getting each number and its index
        for i, num in enumerate(nums):

            # 3. Check if the current number already exists
            if num in dicc:

                # 4. Retrieve the previous index and calculate the distance
                distance = abs(dicc[num] - i)

                # 5. Check if the distance is less than or equal to k
                if distance <= k:
                  return True
        
            # 6. Store or update the number and its current index
            dicc[num] = i
      

        # 7. Return False if no valid pair is found
        return False
