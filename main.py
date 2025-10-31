import sys as sys

from stats import count_characters, count_word, sort_dict


def get_book_text(path_to_file: str):
    with open(path_to_file) as f:
        file_content = f.read()
        if not file_content:
            raise Exception("empty file")
        return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    name = sys.argv[1]
    text = get_book_text(name)
    nb_words = count_word(text)
    s_dict = sort_dict(count_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {name}...")
    print("----------- Word Count ----------")
    print(f"Found {nb_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(s_dict)):
        if s_dict[i]["char"].isalpha():
            print(f"{s_dict[i]['char']}: {s_dict[i]['num']}")
    print("============= END ===============")


main()
