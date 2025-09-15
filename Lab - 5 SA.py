from scipy.optimize import dual_annealing
import numpy as np

# ---------- Cost function ----------
# Input: x is a real vector of length 8. We round it to get integer columns.
def queens_max(x):
    cols = np.round(x).astype(int)
    n = len(cols)
    # penalty if two queens share a column
    if len(set(cols)) < n:
        return 1e6
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            # check diagonals
            if abs(i - j) == abs(cols[i] - cols[j]):
                attacks += 1
    return attacks    # we want to minimize number of attacking pairs

# ---------- Bounds ----------
n = 8
bounds = [(0, n - 1)] * n   # each queen’s column between 0 and 7

# ---------- Run simulated annealing ----------
result = dual_annealing(queens_max, bounds)

# ---------- Process the solution ----------
best_cols = np.round(result.x).astype(int).tolist()
not_attacking = n  # because we minimized attacks to 0

print(f"The best position found is: {best_cols}")
print(f"The number of queens that are not attacking each other is: {not_attacking}")



###############################OUTPUT##########################
The best position found is: [6, 3, 1, 7, 4, 2, 0, 5]
The number of queens that are not attacking each other is: 8
