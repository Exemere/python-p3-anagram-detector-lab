class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        words = [w.lower() for w in words]
    
        anagrams = [w for w in words if self.is_anagram(w)]
        
        return anagrams

   
