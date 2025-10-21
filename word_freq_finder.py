import string
from collections import Counter
import csv

def clean_text(text):
    """Convert to lowercase and remove punctuation."""
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, "")
    return text

def count_words(text):
    """Split text into words and count frequency."""
    words = text.split()
    return Counter(words)

def display_results(counter):
    """Display word frequency in a readable format."""
    print("\nWord Frequency:\n" + "-" * 25)
    for word, freq in counter.items():
        print(f"{word}: {freq}")

def highlight_most_frequent(counter):
    """Highlight the most frequent word."""
    if counter:
        word, freq = counter.most_common(1)[0]
        print(f"\nMost Frequent Word: '{word}' (appears {freq} times)")

def export_to_csv(counter, filename="word_frequency.csv"):
    """Export word-frequency pairs to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Frequency"])
        for word, freq in counter.items():
            writer.writerow([word, freq])
    print(f"\n✅ Results exported to '{filename}'")

def show_histogram(counter):
    """Display a simple text-based histogram."""
    print("\nHistogram (Word Frequency):\n" + "-" * 35)
    for word, freq in counter.most_common():
        print(f"{word:15} | {'#' * freq}")

def main():
    print("=== Word Frequency Counter ===\n")
    
    # Step 1: Get paragraph input
    paragraph = input("Enter a paragraph of text:\n")
    
    # Step 2: Clean and process text
    cleaned_text = clean_text(paragraph)
    counter = count_words(cleaned_text)
    
    # Step 3: Display results
    display_results(counter)
    
    # Step 4: Highlight most frequent word
    highlight_most_frequent(counter)
    
    # Optional: Export to CSV
    choice = input("\nWould you like to export the results to a CSV file? (y/n): ").strip().lower()
    if choice == "y":
        export_to_csv(counter)
    
    # Optional: Show histogram
    choice = input("Would you like to display a histogram? (y/n): ").strip().lower()
    if choice == "y":
        show_histogram(counter)

if __name__ == "__main__":
    main()
