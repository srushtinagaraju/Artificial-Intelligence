import itertools
from sympy import symbols, sympify

# Define propositional symbols
A, B, C = symbols('A B C')

# Ask user for input expressions
alpha_input = input("Enter alpha (example: A | B): ")
kb_input = input("Enter KB (example: (A | C) & (B | ~C)): ")

# Convert input strings into sympy logical expressions
alpha = sympify(alpha_input, evaluate=False)
kb = sympify(kb_input, evaluate=False)

# ANSI escape codes for colors
GREEN = "\033[92m"
RESET = "\033[0m"

# Generate truth table
print(f"\nTruth Table for α = {alpha_input}, KB = {kb_input}\n")
print(f"{'A':<6}{'B':<6}{'C':<6}{'α':<10}{'KB':<10}")

entailed = True  # assume KB |= α holds until proven otherwise

for values in itertools.product([False, True], repeat=3):
    subs = {A: values[0], B: values[1], C: values[2]}
    alpha_val = alpha.subs(subs)
    kb_val = kb.subs(subs)

    # Green highlight if KB is true
    alpha_str = f"{GREEN}{alpha_val}{RESET}" if kb_val else str(alpha_val)
    kb_str = f"{GREEN}{kb_val}{RESET}" if kb_val else str(kb_val)

    # Print row
    print(f"{str(values[0]):<6}{str(values[1]):<6}{str(values[2]):<6}"
          f"{alpha_str:<10}{kb_str:<10}")


    ################OUTPUT######################
Enter alpha (example: A | B): ( A | B)
Enter KB (example: (A | C) & (B | ~C)): (A | C) & (B | ~C)

Truth Table for α = ( A | B), KB = (A | C) & (B | ~C)

A     B     C     α         KB        
False False False False     False     
False False True  False     False     
False True  False True      False     
False True  True  TrueTrue
True  False False TrueTrue
True  False True  True      False     
True  True  False TrueTrue
True  True  True  TrueTrue

 KB |= α holds (KB entails α)

    # Check entailment
    if kb_val and not alpha_val:
        entailed = False

# Final entailment check
if entailed:
    print(f"\n KB |= α holds (KB entails α)\n")
else:
    print(f"\n KB does NOT entail α\n")
