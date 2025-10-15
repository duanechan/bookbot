def get_num_words(text):
    words = set(text.split())
    return f"Found {len(words)} total words"

def count_characters(text):
    char_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count