import sys

from stats import get_num_words, count_characters, sorted_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

word_count = get_num_words(path_to_book)
character_count = count_characters(path_to_book)

def main():
    sorted_result = sorted_count(character_count)

   
    print("============ BOOKBOT ============")
    print(f"Analyzing book...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_result:
        print(f"{entry['character']}: {entry['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()