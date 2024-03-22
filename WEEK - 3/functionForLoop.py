def print_multiplication_table(number, limit):
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

print_multiplication_table(13, 20)