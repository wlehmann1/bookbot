from stats import number_of_words

def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    print()
    text = get_book_text(book_path)
    #print(text)
    print(f"{number_of_words(text)} words found in the document.")
    print()
    letters = character_counts(text)
    letters.sort(reverse=True, key=sort_on)
    for item in letters:
        print(f"The '{item["letter"]}' character was found {item["num"]} times.")
    print()
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_counts(string):
    result = []
    letters = {}
    lowered_string = string.lower()
    for char in lowered_string:
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
    for key, value in letters.items():
        result.append({"letter": key, "num": value})
    return result

main()