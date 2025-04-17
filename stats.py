def get_num_words(path):
 with open(path,"r") as file:
    file.contents = file.read()
    split = file.contents.split()
    num_words = len(split)
    return num_words
    


def count_characters(path):
    with open(path, "r") as file:
        text = file.read()

    character_counts = {}
    for char in text:
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1 

    return character_counts  


def sorted_count(character_counts):
    result = []
    for character, count in character_counts.items():
        if character.isalpha():
            result.append({"character": character, "count": count})


    result = sorted(result, key=lambda x: (x['count']), reverse=True)
    return result


