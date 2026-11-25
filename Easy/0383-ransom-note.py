class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Validate lenght
        if len(ransomNote) > len(magazine):
          return False

        # Create empty dictionary
        frequency = {}

        # Go through magazine and count frequency
        for letter in magazine:
          if letter in frequency:
            frequency[letter] += 1
          else:
            frequency[letter] = 1
            
        # Go through ransomNote
        for letter in ransomNote:

            # Validate if letter does not exist or if it is empty
            if letter not in frequency or frequency [letter] == 0:
              return False

            # Substract 1 from the dictionary letter
            else:
              frequency[letter] -= 1

        return True    
