import numpy as np

# Создание одномерного массива
arr1d = np.array([1, 2, 3, 4, 5])

# Создание двумерного массива
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Создание массива с нулями
zeros_arr = np.zeros((3, 4))

# Создание массива со случайными числами
random_arr = np.random.rand(2, 3)

# Арифметические операции с массивами
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2
sub_arr = arr1 - arr2
mul_arr = arr1 * arr2
div_arr = arr1 / arr2

# Транспонирование массива
arr = np.array([[1, 2], [3, 4]])
transposed_arr = arr.T

# Срезы массива
arr = np.array([1, 2, 3, 4, 5])
sliced_arr = arr[1:4]

# Вывод результатов
print("sum_arr:", sum_arr)
print("sub_arr:", sub_arr)
print("mul_arr:", mul_arr)
print("div_arr:", div_arr)
print("transposed_arr:", transposed_arr)
print("sliced_arr:", sliced_arr)

# Сумма элементов массива
arr = np.array([1, 2, 3, 4, 5])
sum_arr = np.sum(arr)

# Среднее значение элементов массива
mean_arr = np.mean(arr)

# Максимальное и минимальное значения массива
max_val = np.max(arr)
min_val = np.min(arr)
