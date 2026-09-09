import numpy as np  # NumPy library import kar rahe hain

# Students ke original marks array mein store kar rahe hain
marks = np.array([70, 80, 90])

bonus_marks = 5  # Har student ko 5 grace marks dene hain

# NumPy broadcasting se har marks mein 5 automatically add ho jayega
updated_marks = marks + bonus_marks

print("Original Marks:", marks)  # Original marks print
print("Updated Marks:", updated_marks)  # Grace marks ke baad updated marks print