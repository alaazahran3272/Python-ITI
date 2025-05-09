
def print_right_aligned_star_array(height):
    y = [" "] * height
    for i in range(len(y)):
        y[height - 1 - i] = "*"
        print(y)

def pyramid(height):
    lines = []
    for i in range(1, height + 1):
        spaces = height - i
        blocks = i
        lines.append(" " * spaces + "*" * blocks)
    return lines
