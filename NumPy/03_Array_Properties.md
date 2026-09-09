# Array Properties

## Important Properties

### shape
Array ki rows aur columns batata hai.

```python
import numpy as np
arr = np.array([[10,20,30],[40,50,60]])
print(arr.shape)
```

Output: `(2, 3)`

### size
Total elements batata hai.

```python
print(arr.size)
```

Output: `6`

### ndim
Number of dimensions batata hai.

```python
print(arr.ndim)
```

### dtype
Data type batata hai.

```python
print(arr.dtype)
```

## Practice
1. Create a 3x3 array.
2. Print shape, size, ndim and dtype.
3. Change values to float and check dtype.