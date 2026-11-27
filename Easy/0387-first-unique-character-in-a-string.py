
class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Create an empty dictionary
        dicc = {}

        # Iterate through the string, getting each character and its index
        for i, letter in enumerate(s):
            # If the character already exists in the dictionary, increase its frequency by 1
            if letter in dicc:
                dicc[letter] += 1
            # Otherwise, initialize its frequency to 1
            else:
                dicc[letter] = 1

        # Iterate through the string again, getting each character and index
        for i, letter in enumerate(s):

            # Check if the current character has a frequency of 1
            if dicc[letter] == 1:

                # 5. Return its index
                return i

        # 6. Return -1 if no unique character is found
        return -1
