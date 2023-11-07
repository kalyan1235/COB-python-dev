from collections import Counter
import string

def count_unique_words(file_path):
    unique_words = set()
    word_counts = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            words = line.strip().translate(str.maketrans('', '', string.punctuation)).lower().split()
            unique_words.update(words)
            word_counts.update(words)

    return unique_words, word_counts

if _name_ == "_main_":
    file_path = "unq_word.txt"  # Replace with your text file path
    unique_words, word_counts = count_unique_words(file_path)

    print("Unique Words:")
    for word in sorted(unique_words):
        print(word)

    print("\nWord Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")