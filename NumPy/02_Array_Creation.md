# NumPy Array Creation

## Definition

NumPy provides multiple functions to create arrays depending on the requirement.

## Important Functions

### 1. np.array()

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)
```

**Output**

```
[10 20 30 40]
```

### 2. np.zeros()

Creates an array filled with zero.

```python
arr = np.zeros((2, 3))
print(arr)
```

### Output

```
[[0. 0. 0.]
 [0. 0. 0.]]
```

### 3. np.ones()

```python
arr = np.ones((2, 2))
print(arr)
```

### 4. np.full()

Creates an array with the same value.

```python
arr = np.full((2, 3), 7)
print(arr)
```

### 5. np.arange()

Creates values using start, stop and step.

```python
arr = np.arange(0, 10, 2)
print(arr)
```

**Output**

```
[0 2 4 6 8]
```

### 6. np.linspace()

Creates equally spaced values.

```python
arr = np.linspace(0, 10, 5)
print(arr)
```

### 7. np.eye()

Creates an identity matrix.

```python
arr = np.eye(3)
print(arr)
```

## Real-Life Example

- zeros → initial sensor data
- ones → default flags
- full → fixed temperature/value matrix
- arange → sequence generation
- linspace → scientific measurements
- eye → matrix calculations

## Practice

1. Create a 3x3 zero matrix.
2. Create a 2x4 one matrix.
3. Create numbers from 1 to 20 with step 2.
4. Create 10 equally spaced values from 0 to 100.

## Summary

Important functions:

`np.array()`  
`np.zeros()`  
`np.ones()`  
`np.full()`  
`np.arange()`  
`np.linspace()`  
`np.eye()`