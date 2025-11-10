FACTS = [
    "is_darjeeling"
]

RULES = {
    "ice_creams_available": ["is_holiday_spot"],
    "is_holiday_spot": ["is_darjeeling"]
}

BACKTRACKING_GRAPH = {}

def prove(goal, path=[]):
    if goal in FACTS:
        return True

    if goal in path:
        print(f"CYCLE detected: {path + [goal]}")
        return False

    new_path = path + [goal]

    if goal in RULES:
        conditions = RULES[goal]

        all_conditions_met = True
        current_subgoals = []
        print(f"\nTrying to prove Goal: **{goal}** (Requires: {conditions})")

        for condition in conditions:
            if prove(condition, new_path):
                current_subgoals.append(condition)
            else:
                all_conditions_met = False
                print(f"Backtracking: **{condition}** failed, so **{goal}** fails via this rule.")
                break

        if all_conditions_met:
            BACKTRACKING_GRAPH[goal] = current_subgoals
            print(f"Goal **{goal}** PROVEN.")
            return True

    return False


QUERY = "ice_ creams_available"
print(f"Starting Backward Chaining for Query: '{QUERY}' ")
result = prove(QUERY)
print("")

if result:
    print(f"\n Result: The query '{QUERY}' is PROVEN.")
else:
    print(f"\n Result: The query '{QUERY}' could not be proven.")
    
print("\n Final Proof/Backtracking Graph (Goal -> Subgoals) ")
print(BACKTRACKING_GRAPH)





####################OUTPUT#####################
Starting Backward Chaining for Query: 'ice_creams_available' 

Trying to prove Goal: **ice_creams_available** (Requires: ['is_holiday_spot'])

Trying to prove Goal: **is_holiday_spot** (Requires: ['is_darjeeling'])
Goal **is_holiday_spot** PROVEN.
Goal **ice_creams_available** PROVEN.


 Result: The query 'ice_creams_available' is PROVEN.

 Final Proof/Backtracking Graph (Goal -> Subgoals) 
{'is_holiday_spot': ['is_darjeeling'], 'ice_creams_available': ['is_holiday_spot']}
