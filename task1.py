import sys

# перевірка наявності аргументу - шляху до вхідного файлу
if len(sys.argv) != 2:
    print("Usage: python reverse_file.py <input_file_path>")
    sys.exit(1)

input_file_path = sys.argv[1]

# перевірка наявності вхідного файлу та зчитування його даних
try:
    with open(input_file_path, "r") as input_file:
        data = input_file.read()
except FileNotFoundError:
    print(f"Error: file '{input_file_path}' not found.")
    sys.exit(1)

# запис даних у зворотньому порядку до вихідного файлу
with open("reversed.txt", "w") as output_file:
    output_file.write(data[::-1])
