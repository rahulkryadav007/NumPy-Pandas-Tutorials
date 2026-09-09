# NumPy Indexing

## Definition
Indexing se array ke specific element ko access karte hain.

## 1D Array

```python
import numpy as np
arr = np.array([10,20,30,40,50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

### Hinglish
Indexing 0 se start hoti hai. Negative indexing end se start hoti hai.

## 2D Array

```python
arr = np.array([[10,20,30],[40,50,60]])

print(arr[0,1])
print(arr[1,2])
```

### Real-Life
Student marks table mein specific student aur specific subject ka marks access karna.

## Practice
1. Print first element.
2. Print last element.
3. Print middle element.
4. Access 2D array ka second row, third column.