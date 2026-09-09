import numpy as np  # NumPy library import kar rahe hain

# 1D array create kar rahe hain
arr = np.array([10, 20, 30, 40, 50, 60])

print("Index 1 to 3:", arr[1:4])  # Index 1 se 3 tak values access
print("First 3:", arr[:3])  # Starting se first 3 values access
print("From index 3:", arr[3:])  # Index 3 se end tak values access
print("Every second:", arr[::2])  # Har second value access
print("Reverse:", arr[::-1])  # Array ko reverse order mein print