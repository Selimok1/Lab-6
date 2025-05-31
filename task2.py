import pandas as pd

data = pd.read_csv('students.csv')
filtered_students = data[data['Score'] > 80]

sorted_students = filtered_students.sort_values(by='Score', ascending=False) # Сортируем их по убыванию балла

print("Студенты с баллом выше 80, отсортированные по убыванию:")
print(sorted_students)

oldest_student = data.loc[data['Age'].idxmax()]

youngest_student = data.loc[data['Age'].idxmin()]

print(f"\nСамый старший студент: {oldest_student['Name']}, Возраст: {oldest_student['Age']}")
print(f"Самый младший студент: {youngest_student['Name']}, Возраст: {youngest_student['Age']}")