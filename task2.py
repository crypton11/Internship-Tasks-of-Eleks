import sys

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if len(sys.argv) != 2:
    print("Usage: python fibonacci.py <index>")
    sys.exit(1)

try:
    index = int(sys.argv[1])
except ValueError:
    print("Error: index must be an integer.")
    sys.exit(1)

if index < 0:
    print("Error: index must be non-negative.")
    sys.exit(1)

result = fibonacci_recursive(index)
print(f"The {index}-th Fibonacci number is {result}.")
