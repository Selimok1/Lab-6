import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')

plt.figure(figsize=(10, 5)) # Построим гистограмму распределения баллов
plt.hist(data['Score'], bins=10, color='blue', edgecolor='black')
plt.title('Распределение баллов')
plt.xlabel('Баллы')
plt.ylabel('Частота')
plt.grid(axis='y')
plt.show()

average_scores = data.groupby('Group')['Score'].mean().reset_index()

plt.figure(figsize=(10, 5)) # Создаем столбчатую диаграмму среднего балла по группам
plt.bar(average_scores['Group'], average_scores['Score'], color='orange')
plt.title('Средний балл по группам')
plt.xlabel('Группы')
plt.ylabel('Средний балл')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()