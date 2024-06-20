
def main():
    file_path = "books/frankestein.txt"
    file_text = read_book_text(file_path)
    total_words = count_words(file_text)
    print(total_words)
    
    chars_counter = count_characters_usage(file_text)
    
    char_count_list = convert_dict_to_list(chars_counter)
    
    char_count_list.sort(reverse=True, key=sort_on)
    
    print_book_analysis(char_count_list,total_words)
    
    
    

def count_words(text):
    words_list = text.split()
    return len(words_list)

def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters_usage(text):
    lower_text = text.lower()
    char_and_counts = {}
    for ch in lower_text:
        if ch in char_and_counts:
            char_and_counts[ch] += 1
        else:
            char_and_counts[ch] = 1
    return char_and_counts

# to sort a list of dictionaries with given key
def sort_on(dict):
    return dict["count"]

def convert_dict_to_list(dict):
    chars_count_list = []
    for key, value in dict.items():
        
        if key.isalpha():
            chars_count_list.append({
                "char":key,
                "count":value
            })
        
    return chars_count_list

def print_book_analysis(char_count_list, words_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")
    
    for dict in char_count_list:
        print(f"The '{dict['char']}' character was found {dict['count']} times")
    
    print("--- End report ---")

main()