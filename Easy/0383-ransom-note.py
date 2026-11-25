class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Validate length: if ransomNote length is higher, then it is impossible to make that word with the letters from magazine
        if len(ransomNote) > len(magazine):
          return False

        # Create an empty dictionary
        frequency = {}

        # Go through each letter of magazine and count frequency
        for letter in magazine:
          if letter in frequency:
            frequency[letter] += 1
          else:
            frequency[letter] = 1
            
        # Go through each letter of ransomNote
        for letter in ransomNote:

            # Validate if the letter does not exist or if it is empty, return False because we cannot make the word with magazine letters
            if letter not in frequency or frequency [letter] == 0:
              return False

            # Subtract 1 from the dictionary letter to update the dictionary letter count 
            else:
              frequency[letter] -= 1
        #If all letters from ransomNote are found in magazine, return True 
        return True    
