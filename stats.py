def get_word_count(content):
    result_info = content.split()
    return len(result_info)

def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_logic(dict):
    return dict["num"]

def sorted_format(letter_dict):
    converted = [{"char": k, "num": v} for k, v in letter_dict.items()]
    converted.sort(key=sort_logic, reverse=True)
    return converted
    