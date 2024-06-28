print("hello world")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)

def count_characters(text):
    lowercased_test = text.lower()
    joined_string = ''.join(lowercased_test.split())

    new_dict = {}
    for char in joined_string:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    
    return new_dict

def sort_on(dict_item):
    return dict_item["count"]

def list_convert(dict):
    return [{'char': key, 'count': value} for key, value in dict.items()]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    characters_dict = count_characters(text)
    converted_dict_list = list_convert(characters_dict)
    converted_dict_list.sort(reverse=True, key=sort_on)
    first_line = f"--- Begin report of {book_path} ---"
    second_line = f"{count} words found in the document"
    
    char_lines = []
    for item in converted_dict_list:
        formatted_string = f"The '{item['char']}' character was found {item['count']} times"
        char_lines.append(formatted_string)

    last_line = f"--- End report ---"
    print(first_line)
    print(second_line)
    for line in char_lines:
        print(line)
    print(last_line)
    

if __name__ == "__main__":
    main()