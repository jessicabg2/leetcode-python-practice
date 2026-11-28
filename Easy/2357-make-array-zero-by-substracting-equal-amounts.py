class Solution:
    def minimumOperations(self, nums: list[int]) -> int:

        #Define set to eliminate duplicate numbers of the list
        arr = set (nums)
        #Dicard 0
        arr.discard(0)
        #Count the numbers of unique elements in the set 
        return len(arr)
