def print_custom_multiplication_table(number, start_multiplier, end_multiplier):
    print(f"Now computing times tables for {number}:")
    for i in range(start_multiplier, end_multiplier + 1):
        result = number * i
        print(f"{number} x {i} = {result}")
    print("Finished computing.")

while True:
    number = int(input("Enter the number you want to compute multiples of (enter 0 to exit): "))
    if number == 0:
        break
    start_multiplier = int(input("Enter the start multiplier: "))
    end_multiplier = int(input("Enter the end multiplier: "))
    print_custom_multiplication_table(number, start_multiplier, end_multiplier)