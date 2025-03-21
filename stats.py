def word_count(book_file):  #function designed to take a string and return the number of words it contains
    count = 0
    words = book_file.split()
    for word in words:
        count += 1
    return count

def char_count(book_file):  #function designed to take a string and return a dictionary containing each unique character found as a key with the number of times it appears as the corresponding value
    char_index = {}
    for char in book_file.lower():
        if char not in char_index:
            char_index[char] = 1
        else:
            char_index[char] += 1
    return char_index

def char_sort(char_dict):  #function designed to take a dictionary and return it as a list of sorted dictionaries
    dict_list = []
    for index in char_dict:  #for every key:value pair in the provided dictionary makes a new dictionary with the new key "char" set to the old key, and the new key "count" set to the old value
        new_dict = {
            "char" : index,
            "count" : char_dict[index]        
                    }
        dict_list.append(new_dict)

    def get_key(dict):  #function designed to create a key for the .sort function
        return dict["count"]
    
    dict_list.sort(reverse=True, key=get_key)  #sorts the list of dictionaries created by the number of times each character was found
    return dict_list