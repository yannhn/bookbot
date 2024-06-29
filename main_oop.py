class Bookbot:
    def __init__(self, path):
        self.path = path
    
    def read_book(self):
        with open(self.path) as f:
            return f.read()
        
    def count_words(self):
        base_text = self.read_book()
        splitted_text = base_text.split()
        return len(splitted_text)
    
    def count_characters(self):
        base_text = self.read_book()
        lower_text = base_text.lower()
        joined_string = ''.join(lower_text.split())

        new_dict = {}
        for item in joined_string:
            if item in new_dict:
                new_dict[item] += 1
            else:
                new_dict[item] = 1
        
        return new_dict
    
    def sort_on(self,dict_item):
        return dict_item['count']

    def organize_dict(self):
        setup_dict = self.count_characters()

        new_list = []
        for key, value in setup_dict.items():
            new_dict = {'char': key, 'count': value}
            new_list.append(new_dict)
        return new_list
    
    def report(self):
        
        first_line = f"--- Begin report of {self.path} ---"
        second_line = f"{self.count_words()} words found in the document"

        base_dict = self.organize_dict()
        base_dict.sort(reverse=True, key=self.sort_on)

        char_lines = []
        for item in base_dict:
            formatted_string = f"The '{item['char']}' character was found {item['count']} times"
            char_lines.append(formatted_string)

        last_line = f"--- End report ---"

        print(first_line)
        print(second_line)
        for line in char_lines:
            print(line)
        print(last_line)


frankenstein = Bookbot('books/frankenstein.txt')


frankenstein.report()


