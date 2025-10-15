def get_num_words(text: str):
    words = text.split()
    return len(words)

def get_character_counts(text: str):
    char_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count

def sort_character_counts(character_counts: dict[str, int]):
    def sort_on(items: list):
        return items["num"]
    
    sorted_list = []

    for c in character_counts:
        sorted_list.append({"char": c, "num": character_counts[c]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list