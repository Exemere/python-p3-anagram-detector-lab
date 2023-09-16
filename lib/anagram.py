class Anagram:
    def __init__(self, word):
        self.word = word.lower()  

    def match(self, word_list):
        
        word_list = [w.lower() for w in word_list]
        
        
        anagrams = [w for w in word_list if self.is_anagram(w)]
        
        return anagrams

    def is_anagram(self, other_word):
        
        return sorted(self.word) == sorted(other_word)


