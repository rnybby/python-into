def print_upper_words(words):
    """prints out a list of uppercased words"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """prints out words that starts with an uppercased 'E' or lowercased 'e' """
    for word in words:
        if word.startswith('e')  or word.startswith('E'):
            print(word.upper())

 

def print_upper_words3(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
               print(word.upper())
        


