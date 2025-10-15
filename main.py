from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(get_num_words(file_contents))

main()