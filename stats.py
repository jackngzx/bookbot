def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    characters = list(text.lower())
    num_chars = {}
    for character in characters:
        if character in num_chars:
            num_chars[character] += 1
        else:
            num_chars[character] = 1

    return num_chars

def sorted_on(items):
    return items["num"]
    
def sorted_num_chars(text):  
    sorted_list = []

    #getting unsorted list    
    unsorted = get_num_chars(text)
    for character in unsorted:
        num = unsorted[character]
        sorted_list.append({"char": character, "num": num})

    sorted_list.sort(reverse=True, key=sorted_on)
    return sorted_list