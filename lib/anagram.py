#START
#match instance method should take a list of words and iterate over the list
#match should iterate over the letters in each word
#match should compare each list of sorted letters
#if they match, add that word to the list
#if they don't match, don't add that word to the list

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        match_list = []
        for word in words_list:
            letter_list =[]
            for letter in word:
                letter_list.append(letter)
                if sorted(letter_list) == sorted(list(self.word)):
                    match_list.append(word)
        return match_list
        