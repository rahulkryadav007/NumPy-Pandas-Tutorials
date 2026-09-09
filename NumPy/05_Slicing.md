# NumPy Slicing

## Definition
Slicing se array ke multiple elements ko access karte hain.

## Syntax

```python
array[start:stop:step]
```

## Examples

```python
import numpy as np
arr = np.array([10,20,30,40,50,60])

print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[::2])
print(arr[::-1])
```

### Explanation
- `arr[1:4]` → index 1 to 3
- `arr[:3]` → starting se index 2 tak
- `arr[3:]` → index 3 se end tak
- `arr[::2]` → every second element
- `arr[::-1]` → reverse array

## Practice
Reverse an array using slicing.