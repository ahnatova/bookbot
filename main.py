def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    number_of_characters = get_num_chararacters(text)
    converted_dict = convert_dict_to_list(number_of_characters)
    converted_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()  # Add an empty line for better readability
    for char_dict in converted_dict:
        if char_dict['character'].isalpha():  # Only print alphabetic characters
            print(f"The '{char_dict['character']}' character was found {char_dict['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        new_dict = {
            "character": char,
            "num": count
        }
        char_list.append(new_dict)
    return char_list

def get_num_chararacters(text):
    lowered_text = text.lower()
    characters = {}
    for c in lowered_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1       
    return characters

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()