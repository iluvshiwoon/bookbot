def count_word(text: str):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_characters(text: str):
    r = {}
    for character in text:
        l_character = character.lower()
        if l_character not in r:
            r[l_character] = 1
        else:
            r[l_character] += 1
    return r


def helper_sort(character_count):
    return character_count["num"]


def sort_dict(character_count):
    r_list = []
    for key in character_count:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = character_count[key]
        r_list.append(new_dict)
    r_list.sort(reverse=True, key=helper_sort)
    return r_list
