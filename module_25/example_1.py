import numpy as np
import matplotlib.pyplot as plt

# Задаем имитационные данные (возраст и уровень холестерина)
age = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
cholesterol = np.array([180, 190, 200, 210, 220, 230, 240, 250, 260, 270])

# Построение аппроксимирующей модели (линейная аппроксимация)
coefficients = np.polyfit(age, cholesterol, 1)
polynomial = np.poly1d(coefficients)

# Создание новых данных для прогнозирования
new_age = np.array([80, 85, 90])

# Прогнозирование уровня холестерина на основе модели
predicted_cholesterol = polynomial(new_age)

# Визуализация результатов
plt.scatter(age, cholesterol, label='Исходные данные')
plt.plot(new_age, predicted_cholesterol, label='Прогноз')
plt.xlabel('Возраст')
plt.ylabel('Уровень холестерина')
plt.legend()
plt.show()