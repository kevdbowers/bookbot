def word_count(book_file):
    count = 0
    words = book_file.split()
    for word in words:
        count += 1
    return count

def char_count(book_file):
    char_index = {}
    for char in book_file.lower():
        if char not in char_index:
            char_index[char] = 1
        else:
            char_index[char] += 1
    return char_index

def char_sort(char_dict):
    dict_list = []
    for index in char_dict:
        new_dict = {
            "char" : index,
            "count" : char_dict[index]        
                    }
        dict_list.append(new_dict)

    def get_key(dict):
        return dict["count"]
    
    dict_list.sort(reverse=True, key=get_key)
    return dict_list