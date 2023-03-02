import sys
import string

# визначення імені вхідного файлу з аргументів командного рядка
if len(sys.argv) != 2:
    print("Usage: python word_frequency.py filename")
    sys.exit(1)
filename = sys.argv[1]

# відкриття вхідного файлу та читання його вмісту
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")
    sys.exit(1)

# заміна знаків пунктуації та перетворення тексту на список слів
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.lower().split()

# створення словника для зберігання частоти вживання слів
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# виведення слів та їх частоти від найбільш до найменш вживаних
sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)
for word in sorted_words:
    print(f"{word}: {word_freq[word]}")
