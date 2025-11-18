### IMPORTS ###
import sys
from stats import *

### FUNCTIONS ###

# 1. Get Book Text:  It takes a filepath as input and returns the contents of the file as a string
def get_book_text(fp):
    with open(fp) as f:
        return f.read()
    
# 2. Print report of chosen book to the terminal
def print_report(dict_ls, title, sub1, sub2, sub3, path, num_words):
    ### HEADER PRINTING ###
    print_header(path, num_words)
    ### DATA PRINTING ###
    for dict in dict_ls:
        print(f"{dict["name"]}: {dict["num"]}")
    ### FOOTER PRINTING ###
    print_footer(sub3)

# Main Program
#   1. Takes input path to desired book from sys.argv
#   2. Creates Word List
#   3. Gets number of words in the book
#   4. Creates dictionary of all characaters and occurences listed in the book
#   5. Prints a report to the terminal

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        title = "BOOKBOT"
        wc_str = "Word Count"
        cc_str = "Character Count"
        end_str = "END"
        book_contents = get_book_text(book_path)
        word_list = get_word_list(book_contents)
        num_words = get_num_words(book_contents)
        dict_list = sort_dict(get_occur_count(word_list))
        print_report(dict_list, title, wc_str, cc_str, end_str, book_path, num_words)

# Calls main function to begin execution
main()