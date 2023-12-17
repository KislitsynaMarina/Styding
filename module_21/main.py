import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Загрузка данных
data = pd.read_csv('data.csv')

# Очистка данных
data = data.drop_duplicates()  # Удаление дубликатов
data = data.dropna()  # Удаление пропущенных значений

# Подготовка данных для обучения
X = data.drop('target', axis=1)  # Входные признаки
y = data['target']  # Целевая переменная

# Масштабирование признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

