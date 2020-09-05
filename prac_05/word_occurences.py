
"""word occurences"""

"""CONSTANTS"""

"""Main"""

def main():

    user_string = input("Test: ")
    each_word = count_words(user_string)
    display_words_and_count(each_word)

"""other functions"""

def count_words(user_string):   #does the math and forms the dictionary
    each_word = {}
    words = user_string.split()
    for i in words:
        number_of_times = each_word.get(i, 0)
        each_word[i] = number_of_times + 1
    return each_word

def display_words_and_count(each_word):     #formatts and prints the dictioanry
    list_words = list(each_word.keys())
    list_words.sort()

    longest_word = max((len(word) for word in list_words))
    for i in list_words:
        print("{:{}} = {}".format(i, longest_word, each_word[i]))

"""run"""

main()