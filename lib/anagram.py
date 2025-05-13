# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the original word in lowercase to ensure case-insensitive comparison
        self.word = word.lower()
        # Pre-sort the characters in the original word for easy anagram checking
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        # Initialize an empty list to store the matching anagrams
        matches = []
        # Iterate through each word in the provided word list
        for word in word_list:
            # Check if the current word is an anagram of the original word
            if sorted(word.lower()) == self.sorted_word and word.lower() != self.word:
                # If it is, add it to the matches list
                matches.append(word)
        # Return the list of matching anagrams
        return matches
    
# Example usage:
listen = Anagram("gogloe")
print(listen.match(["enlists", "google", "inlets", "banana"])) 