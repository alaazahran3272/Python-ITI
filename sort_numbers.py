
def sort_input_numbers():
    arr = []
    print("Enter 5 numbers:")
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        arr.append(num)

    ascending = sorted(arr)
    descending = sorted(arr, reverse=True)

    print("Ascending order:", ascending)
    print("Descending order:", descending)
