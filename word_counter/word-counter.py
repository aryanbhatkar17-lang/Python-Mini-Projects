import re
import os

def read_file_text(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the path and try again.")
        return ""

def count_word_regex(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def word_frequency(words):
    search_word = input("Enter the word to be searched: ").strip().lower()
    word_freq = words.count(search_word)
    return word_freq, search_word

def display_results(total_words, search_word, word_frequency):
    print(f"\n--- Results ---")
    print(f"Total Words in File: {total_words}")
    print(f"Frequency of '{search_word}': {word_frequency}")

if __name__ == "__main__":
    filename = input("Enter file path that is to be searched: ").strip()
    text = read_file_text(filename)


    if text:
        words = count_word_regex(text)
        total_words = len(words)
        word_freq, search_word = word_frequency(words)
        display_results(total_words, search_word, word_freq)