import numpy as np  # NumPy library import kar rahe hain

# 2D student marks array create kar rahe hain
marks = np.array([
    [80, 75, 90],
    [85, 95, 70]
])

print("Array:")
print(marks)  # Complete array print kar rahe hain

print("Shape:", marks.shape)  # Rows aur columns ki information
print("Size:", marks.size)  # Total elements count
print("Dimensions:", marks.ndim)  # Array kitne dimensions ka hai
print("Data Type:", marks.dtype)  # Values ka data type