from collections import Counter

def read_word_counts(filepath):
    counter = Counter()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                word, count = line.strip().split('\t')
                counter[word] += int(count)
            except ValueError:
                continue  # Skip malformed lines
    return counter

def print_top_n(counter, n=15):
    print(f"\nTop {n} most frequent words:\n" + "-"*30)
    for word, count in counter.most_common(n):
        print(f"{word:20} {count}")

if __name__ == "__main__":
    filepath = "output/part-00000"  # Adjust this if your output file is elsewhere
    word_counts = read_word_counts(filepath)
    print_top_n(word_counts, 15)
