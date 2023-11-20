import re

# Замена с использованием регулярного выражения
text = "Patient ID: 12345, Name: John Doe"
pattern = r"\d+"
replacement = "XXXXX"
result = re.sub(pattern, replacement, text)
print(result)

# Разделение текста с использованием регулярного выражения
text = "apple,orange,banana"
pattern = r","
result = re.split(pattern, text)
print(result)

# Пример: Извлечение даты из текста
text = "Patient was admitted on 2023-07-20 for treatment."
pattern = r"\d{4}-\d{2}-\d{2}"
date = re.search(pattern, text).group()
print(date)  # Output: "2023-07-20"

# Пример: Поиск всех кодов диагнозов в тексте
text = "Patient was diagnosed with ICD-10 codes I25.2 and J45.909."
pattern = r"[A-Z]\d{2}\.\d{1,3}"
diagnosis_codes = re.findall(pattern, text)
print(diagnosis_codes)  # Output: ['I25.2', 'J45.909']

# Пример: Извлечение имени пациента из медицинского отчета
text = "Patient: John Doe, Age: 35, Diagnosis: Hypertension"
pattern = r"Patient: (\w+ \w+)"
patient_name = re.search(pattern, text).group(1)
print(patient_name)  # Output: "John Doe"

# Пример: Извлечение списка лекарств из медицинского отчета
text = "Prescription: Aspirin 100mg, Lisinopril 10mg, Metformin 500mg"
pattern = r"Prescription: ([\w\s\d]+)"
medications = re.search(pattern, text).group(1).split(", ")
print(medications)  # Output: ['Aspirin 100mg', 'Lisinopril 10mg', 'Metformin 500mg']

# Пример: Поиск дат в медицинской документации
text = "Patient was seen on 2023-07-20 and 2023-07-25 for follow-up."
pattern = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(pattern, text)
print(dates)  # Output: ['2023-07-20', '2023-07-25']

# Пример: Поиск кодов диагнозов в анамнезе пациента
text = "Past medical history: Hypertension (ICD-10: I10), Diabetes (ICD-10: E11.9)."
pattern = r"ICD-10: ([A-Z]\d{2}(\.\d{1,3})?)"
diagnosis_codes = re.findall(pattern, text)
print(diagnosis_codes)  # Output: [('I10', ''), ('E11.9', '.9')]

# Пример: Замена персональных данных пациента
text = "Patient: John Doe, SNILS: 123-45-6789"
pattern = r"\d{3}-\d{2}-\d{4}"
redacted_text = re.sub(pattern, "XXX-XX-XXXX", text)
print(redacted_text)  # Output: "Patient: Ivan Ivanovich, SNILS: XXX-XXXXXX"

# Пример: Извлечение имен пациентов из списка текстовых данных
data = """
Patient: John Doe, Age: 35, Diagnosis: Hypertension
Patient: Jane Smith, Age: 40, Diagnosis: Diabetes
"""

pattern = r"Patient: (\w+ \w+)"
patient_names = re.findall(pattern, data)
print(patient_names)  # Output: ['John Doe', 'Jane Smith']

# Пример: Извлечение дат и времени из списка текстовых данных
data = """
Appointment on 2023-07-20 at 14:30
Procedure scheduled for 2023-07-25 at 10:00
"""

pattern = r"\d{4}-\d{2}-\d{2} at \d{2}:\d{2}"
appointments = re.findall(pattern, data)
print(appointments)  # Output: ['2023-07-20 at 14:30', '2023-07-25 at 10:00']

# Пример: Извлечение ICD-10 кодов диагнозов из списка текстовых данных
data = """
Diagnosis: Hypertension (ICD-10: I10)
Diagnosis: Diabetes (ICD-10: E11.9)
"""

pattern = r"ICD-10: ([A-Z]\d{2}(\.\d{1,3})?)"
diagnosis_codes = re.findall(pattern, data)
print(diagnosis_codes)  # Output: [('I10', ''), ('E11.9', '.9')]

# Пример: Извлечение числовых значений из списка текстовых данных
data = "Patient ID: 12345, Height: 175 cm, Weight: 70 kg"
pattern = r"\d+"
numeric_values = re.findall(pattern, data)
print(numeric_values)  # Output: ['12345', '175', '70']