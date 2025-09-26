"""
    This program asks the user to enter 15 numbers and then
    prints if they are even or odd. It validates data input.
"""

NUM_LIST = [] 

print("Please enter 15 numbers.")

for i in range(15):
    while True: # Repeat until input is numeric
        # i + 1 shows the user how many are left
        num = input(f"Enter a number {i+1}/15: ")
        if num.isnumeric():
            NUM_LIST.append(int(num))
            break
        else:
            print(f"Please enter a valid number.")
            

for i in range(15):
    # Create number variable to avoid typing NUM_LIST[i] twice.
    number = NUM_LIST[i] 
    if (number % 2 == 0):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
