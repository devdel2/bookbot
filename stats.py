### FUNCTIONS ###

# 1. Takes in a str of the entire book and splits the strings around whitespace
# to return every word into a list of words
def get_word_list(str):
    return str.split()

# 2. Count Book Words: Recieves a string and returns the number of words in 
# the string
def get_num_words(str):
    word_list = get_word_list(str)
    return len(word_list)

# 3. takes the text from the book as a string, and returns the number of times
# each character, (including symbols and spaces), appears in the string. This 
# will return a dictionary of characters and their counts, where the char is 
# the key and the value is the total number
def get_occur_count(word_list):
    letter_dict = {}
    for word in word_list:
        for char in word:
            l_char = char.lower()
            if l_char in letter_dict:
                letter_dict[l_char] = letter_dict[l_char] + 1
            else:
                letter_dict[l_char] = 1
    return letter_dict

# 4. Helper sort function for using with sort_dict
def sort_on(dict):
    return dict["num"]

# 5. takes the dictionary of characters and their counts and returns a sorted list 
# of dictionaries.
def sort_dict(dict):
    dict_ls = []
    for char in dict:
        dict_ls.append({"name": char, "num": dict[char]})
    dict_ls.sort(reverse=True, key=sort_on)
    return dict_ls

# 6. Prints a title to the terminal
def print_header(book_path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

# 7. prints a footer to the terminal
def print_footer(str):
    print(f"============= {str} ===============")
