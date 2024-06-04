
class Anagram:
    def __init__(self, word):
        self.word = word
        # Other initialization code...

    def match(self, words):
        # Implement logic to find anagrams of self.word in the words list
        # This is a placeholder implementation
        matching_words = []
        for word in words:
            if sorted(word) == sorted(self.word):  # Simple anagram check
                matching_words.append(word)
        return matching_words

