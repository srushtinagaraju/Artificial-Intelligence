
def vacuum_cleaner():
    # Input states of rooms A and B
    state = {
        'A': int(input("Enter state of A (0 for clean, 1 for dirty): ")),
        'B': int(input("Enter state of B (0 for clean, 1 for dirty): "))
    }

    # Input starting location
    location = input("Enter location (A or B): ").upper()
    cost = 0

    # Agent logic
    if state['A'] == 0 and state['B'] == 0:
        print("Turning vacuum off")
    else:
        if location == 'A':
            if state['A'] == 1:
                print("Cleaned A.")
                state['A'] = 0
                cost += 1
            else:
                print("A is clean")

            print("Moving vacuum right")
            if state['B'] == 1:
                print("Cleaned B.")
                state['B'] = 0
                cost += 1
            else:
                print("B is clean")

        elif location == 'B':
            if state['B'] == 1:
                print("Cleaned B.")
                state['B'] = 0
                cost += 1
            else:
                print("B is clean")

            print("Moving vacuum left")
            if state['A'] == 1:
                print("Cleaned A.")
                state['A'] = 0
                cost += 1
            else:
                print("A is clean")

    # Final Output
    print(f"Cost: {cost}")
    print(state)

# Run the function
vacuum_cleaner()


OUTPUT

Enter state of A (0 for clean, 1 for dirty): 1
Enter state of B (0 for clean, 1 for dirty): 1
Enter location (A or B): A
Cleaned A.
Moving vacuum right
Cleaned B.
Cost: 2
{'A': 0, 'B': 0}


Enter state of A (0 for clean, 1 for dirty): 0
Enter state of B (0 for clean, 1 for dirty): 0
Enter location (A or B): B
Turning vacuum off
Cost: 0
{'A': 0, 'B': 0}

Enter state of A (0 for clean, 1 for dirty): 1
Enter state of B (0 for clean, 1 for dirty): 0
Enter location (A or B): A
Cleaned A.
Moving vacuum right
B is clean
Cost: 1
{'A': 0, 'B': 0}

Enter state of A (0 for clean, 1 for dirty): 0
Enter state of B (0 for clean, 1 for dirty): 1
Enter location (A or B): B
Cleaned B.
Moving vacuum left
A is clean
Cost: 1
{'A': 0, 'B': 0}
