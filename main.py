from stats import get_num_words, get_character_counts, sort_character_counts

def print_banner(title: str, border: str, left_padding: int, right_padding: int):
    print(border * left_padding, title, border * right_padding)

def get_book_text(filepath: str = "books/frankenstein.txt"):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        return f.read()

def display_word_count(file_contents: str):
    num_words = get_num_words(file_contents)
    print_banner("Word Count", "-", 11, 10)
    print(f"Found {num_words} total words")

def display_char_count(chars_count):
    print("-" * 9, "Character Count", "-" * 7)
    for e in chars_count:
        if not e["char"].isalpha():
            continue
        print(f"{e["char"]}: {e["num"]}")

def main():
    print_banner("BOOKBOT", "=", 12, 12)
    file_contents = get_book_text()
    display_word_count(file_contents)
    char_count = get_character_counts(file_contents)
    display_char_count(sort_character_counts(char_count))
    print_banner("END", "=", 13, 15)
main()