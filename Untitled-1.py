def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two terms

    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Example usage:
num_terms = 10
fibonacci_sequence = generate_fibonacci(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)
