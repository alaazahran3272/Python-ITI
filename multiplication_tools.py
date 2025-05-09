
def multiplication_tables(x):
    """Prints a triangle-style multiplication table."""
    for i in range(1, x + 1):
        for b in range(1, i + 1):
            print(f"{i}*{b}= {i*b}")


def generate_multiplication_array():
    """Prints a 2D array (list of lists) representation of multiplication values."""
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        row = [i * j for j in range(1, i + 1)]
        print(row)
