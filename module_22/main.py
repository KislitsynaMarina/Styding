import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('medical_data.csv')

# Подготовка данных для обучения
X = data.drop('target', axis=1)  # Входные признаки
y = data['target']  # Целевая переменная

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели классификации
classification_model = DecisionTreeClassifier()
classification_model.fit(X_train, y_train)

# Применение модели для классификации
new_data = pd.DataFrame({'age': [40], 'gender': [2], 'height': [160], 'weight': [65],
                         'ap_hi': [140], 'ap_lo': [90], 'cholesterol': [3], 'gluc': [1],
                         'smoke': [0], 'alco': [0], 'active': [1]})
prediction = classification_model.predict(new_data)
print("Прогнозируемая метка класса:", prediction[0])