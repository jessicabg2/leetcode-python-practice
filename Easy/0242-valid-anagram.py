class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        # Check if both strings have the same length, if not, they cannot be anagrams.
        if len(s) != len(t):
          return False
        # Create empty dictionaries to store letter frequencies
        s_freq = {}
        t_freq = {}

        # Go through s and count the frequencies
        for letter in s:
            if letter in s_freq:
                s_freq[letter] += 1
            else:
                s_freq[letter] = 1

        # Go through t and count the frequencies
        for letter in t:
            if letter in t_freq:
                t_freq[letter] += 1
            else:
                t_freq[letter] = 1

        # Compare dictionaries, if their letter frequencies are identical, return True.
        if s_freq == t_freq:
          return True
        else:
          return False
