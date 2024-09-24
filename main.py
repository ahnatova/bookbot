def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    print(f"The number of words is: {number_of_words}")
    number_of_characters = get_num_chararacters(text)
    print(number_of_characters)

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