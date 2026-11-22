import numpy as np

arr = np.random.randint(0, 10, 10)
print("Original array:", arr)

new_arr= arr.copy()
new_arr[new_arr % 2 != 0] = -1
print("After replacing odd numbers:", new_arr)

arr_2d = arr.reshape(2, 5)
print("2D array:")
print(arr_2d)

print("Sum of all elements:", arr.sum())