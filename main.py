from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(count_characters(file_contents))

main()