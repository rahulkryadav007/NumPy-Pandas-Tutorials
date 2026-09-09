# Copy and View

## Copy
Independent array banata hai.

```python
import numpy as np

arr = np.array([1,2,3])
copy_arr = arr.copy()
copy_arr[0] = 100

print(arr)
print(copy_arr)
```

## View
Original memory ko share karta hai.

```python
view_arr = arr.view()
view_arr[0] = 50
print(arr)
```

## Important
Copy independent hota hai, view original data se connected hota hai.