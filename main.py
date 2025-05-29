from stats import get_word_count, get_character_count, sorted_format
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    result = get_book_text(sys.argv[1])
    word_count = get_word_count(result)
    letter_dict = get_character_count(result.replace(" ", ""))
    sorted_result = sorted_format(letter_dict)
    print(f"""============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------""")

    for letter in sorted_result:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    
    print("============= END ===============")

main()
