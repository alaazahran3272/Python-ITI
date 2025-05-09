
def find_positions_of_i(input_string):
    target_char = 'i'
    return [index for index, char in enumerate(input_string) if char == target_char]
