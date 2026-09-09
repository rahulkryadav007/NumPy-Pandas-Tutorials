import numpy as np  # NumPy library import kar rahe hain

# 2 rows aur 3 columns ka marks array create kar rahe hain
marks = np.array([
    [80, 75, 90],
    [85, 95, 70]
])

print("First Row Second Value:", marks[0, 1])  # Row 0 aur column 1 ki value access
print("Second Row Third Value:", marks[1, 2])  # Row 1 aur column 2 ki value access