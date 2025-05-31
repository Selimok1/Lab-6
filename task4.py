import pandas as pd

data = pd.read_csv('students.csv')
data['Passed'] = data['Score'].apply(lambda x: 1 if x >= 60 else 0)

grouped_data = data.groupby('Group').agg(
    Average_Score=('Score', 'mean'),
    Median_Age=('Age', 'median') # Группируем по 'Group' и вычисляем средний балл и медианный возраст
).reset_index()

print(grouped_data)