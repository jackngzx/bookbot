import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words, get_num_chars, sorted_on, sorted_num_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
         for i in range (1, len(sys.argv)):  
            text = get_book_text(sys.argv[i])
            num_words = get_num_words(text)
            num_chars = get_num_chars(text)
            print(f"Found {num_words} total words")
            
            sorted_list = sorted_num_chars(text)
            for i in sorted_list:
                if i["char"].isalpha() == True:
                    char = i["char"]
                    num = i["num"]
                    print(f"{char}: {num}")

main()