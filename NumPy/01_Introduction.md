# NumPy Introduction 🔢

## 1. What is NumPy?

**NumPy (Numerical Python)** is a Python library used for numerical computing and working with arrays.

### Hinglish Explanation

Simple words mein: jab hume bahut saare numbers par fast calculation karni ho, NumPy bahut useful hota hai.

## 2. Real-Life Example

Socho ek college mein 10,000 students ke marks hain. Hume calculate karna hai:

- Average marks
- Maximum marks
- Minimum marks
- Total marks

NumPy numerical data ko efficiently handle karta hai.

## 3. Installation

```bash
pip install numpy
```

## 4. Import NumPy

```python
import numpy as np
```

### Explanation

- `import` → library ko program mein use karne ke liye.
- `numpy` → library ka actual name.
- `as np` → short name.

## 5. First NumPy Program

```python
import numpy as np

marks = np.array([80, 75, 90, 85, 95])

print(marks)
```

### Output

```
[80 75 90 85 95]
```

### Code Explanation

```python
marks = np.array([80, 75, 90, 85, 95])
```

- `marks` → variable name
- `np` → NumPy alias
- `array()` → array banane ka function
- values → student marks

## 6. Why NumPy?

### Fast Calculations

```python
arr = np.array([10, 20, 30, 40])

print(arr + 10)
```

### Output

```
[20 30 40 50]
```

### Real-Life Meaning

Agar sab students ko 10 grace marks dene hain, NumPy ek operation mein sab values update kar sakta hai.

## 7. NumPy Uses

- Data Analysis
- Machine Learning
- Artificial Intelligence
- Engineering Calculations
- Scientific Computing
- Student and Sales Data Analysis

## 8. Important Preview Operations

```python
arr = np.array([10, 20, 30])

print(arr + 5)
print(arr * 2)
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
```

## Practice Questions

1. Create an array containing 10, 20, 30, 40, 50.
2. Create an array of five student marks.
3. Add 5 grace marks.
4. Find maximum, minimum and average.

## Interview Questions

### What is NumPy?
NumPy is a Python library used for numerical computing and efficient array operations.

### What is the common alias for NumPy?

```python
import numpy as np
```

## Summary

NumPy = **Numerical Python**

It is mainly used for:

✔ Arrays  
✔ Fast calculations  
✔ Data Analysis  
✔ Machine Learning  
✔ Engineering and Scientific Computing