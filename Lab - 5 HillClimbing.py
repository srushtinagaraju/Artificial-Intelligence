import random

def compute_cost(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:               # same row
                cost += 1
            elif abs(state[i] - state[j]) == abs(i - j):  # same diagonal
                cost += 1
    return cost


def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):        # pick a column
        for row in range(n):    # try moving queen in this column to another row
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors



def print_board(state):
    n = len(state)
    for r in range(n):
        line = ""
        for c in range(n):
            line += "Q " if state[c] == r else ". "
        print(line)
    print("")


def hill_climb(initial_state, max_sideways=50):
    current = initial_state
    current_cost = compute_cost(current)
    steps = 0
    sideways_moves = 0

    print("Initial State (cost={}):".format(current_cost))
    print_board(current)

    while True:
        neighbors = get_neighbors(current)
        costs = [compute_cost(n) for n in neighbors]
        min_cost = min(costs)

        if min_cost > current_cost:
            # no better neighbor -> stop
            break

        # pick one of the best neighbors randomly
        best_neighbors = [n for n, c in zip(neighbors, costs) if c == min_cost]
        next_state = random.choice(best_neighbors)
        next_cost = compute_cost(next_state)

        # handle sideways moves
        if next_cost == current_cost:
            if sideways_moves >= max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0

        current = next_state
        current_cost = next_cost
        steps += 1

        print("Step {} (cost={}):".format(steps, current_cost))
        print_board(current)

        if current_cost == 0:
            print("Solution found in {} steps ✅".format(steps))
            return current

    print("Local minimum reached (cost={}) ❌".format(current_cost))
    return current



initial_state = [3, 1, 2, 0]

final = hill_climb(initial_state, max_sideways=10)


######################OUTPUT#######################################
Initial State (cost=2):
. . . Q 
. Q . . 
. . Q . 
Q . . . 

Step 1 (cost=2):
. Q . Q 
. . . . 
. . Q . 
Q . . . 

Step 2 (cost=1):
. Q . . 
. . . Q 
. . Q . 
Q . . . 

Step 3 (cost=1):
. Q . . 
. . . Q 
. . . . 
Q . Q . 

Step 4 (cost=0):
. Q . . 
. . . Q 
Q . . . 
. . Q . 

Solution found in 4 steps ✅
