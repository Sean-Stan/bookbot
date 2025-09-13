def count_words(words):
    list_of_words = words.split()
    return len(list_of_words)

def count_characters(words):
    characters = {}
    for character in words:
        if not character.isalpha():
            continue
        current_character = character.lower()
        if current_character in characters:
            characters[current_character] = characters[current_character] + 1
        else:
            characters[current_character] = 1

    return characters

def sort_character_count(character_count):
    character_count_list = []

    for character in character_count:
        character_count_list.append({'name': character, 'num': character_count[character]})

    sorted_by_num = sorted(character_count_list, key=lambda d: d['num'], reverse=True)

    return sorted_by_num