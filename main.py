def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_letters = get_letter_count(text)
    letter_frequency = get_letter_frequency(text)
    num_sentences = get_sentence_count(text)
    generate_report(book_path, num_words, num_letters, letter_frequency, num_sentences)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
    return sum(letters.values())

def get_letter_frequency(text):
    letters = {}
    for char in text.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
    return dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))

def get_sentence_count(text):
    import re
    sentences = re.split('[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def generate_report(path, num_words, num_letters, letter_frequency, num_sentences):
    print("\n--- Book Report ---")
    print(f"Analyzing file: {path}")
    print(f"\nTotal Words: {num_words}")
    print(f"Total Letters: {num_letters}")
    print(f"Total Sentences: {num_sentences}")
    
    print("\nLetter Frequency (top 5):")
    for char, count in list(letter_frequency.items())[:5]:
        percentage = (count / num_letters) * 100
        print(f"'{char}': {count} ({percentage:.1f}%)")
    
    print(f"\nAverage Words per Sentence: {num_words/num_sentences:.1f}")
    print(f"Average Letters per Word: {num_letters/num_words:.1f}")

if __name__ == "__main__":
    main()
