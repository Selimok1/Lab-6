import pandas as pd

data = pd.read_csv('students.csv') # Загружаем данные

print("Первые 5 строк данных:")
print(data.head())

print("\nИнформация о данных:")
print(data.info())

print("\nСтатистика:")
print(data.describe())

average_score = data['Score'].mean()
print(f"\nСредний балл студентов: {average_score}")

group_counts = data['Group'].value_counts()
print("\nКоличество студентов в каждой группе:")
print(group_counts)