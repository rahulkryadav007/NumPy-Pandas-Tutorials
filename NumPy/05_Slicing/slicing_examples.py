import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Index 1 to 3:", arr[1:4])
print("First 3:", arr[:3])
print("From index 3:", arr[3:])
print("Every second:", arr[::2])
print("Reverse:", arr[::-1])