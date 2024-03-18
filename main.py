#

letters_dict = {}
letters_list = []

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        return file_contents

def word_count():
    with open('books/frankenstein.txt', 'r') as f:
        book_as_string = f.read()
        words = book_as_string.split()
        number_of_words = len(words)
        print(f"Total number of word is {number_of_words}")

def count_letters():
    with open('books/frankenstein.txt') as f:
        book_as_string = f.read()
        lowered_letters = book_as_string.lower()
        for i in lowered_letters:
            if i.isalpha():
                if i in letters_dict:
                    letters_dict[i] += 1
                elif i != letters_dict:
                    letters_dict[i] = 1
        print(letters_dict)

def sort_on(dict):
    return dict["count"]

def book_report():
    with open('books/frankenstein.txt') as f:
        book_as_string = f.read()
        words = book_as_string.split()
        number_of_words = len(words)
        lowered_letters = book_as_string.lower()
        for i in lowered_letters:
            if i.isalpha():
                if i in letters_dict:
                    letters_dict[i] += 1
                elif i != letters_dict:
                    letters_dict[i] = 1
        for i in letters_dict:
            letters_list.append({"letter": i, "count": letters_dict[i]})
        letters_list.sort(reverse=True, key=sort_on)
        print(f"Total number of word is {number_of_words}")
        for i in letters_list:
            print(f"The {i['letter']} character was found {i['count']} times")




main()
#word_count()
#count_letters()
book_report()