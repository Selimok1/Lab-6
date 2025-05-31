import pandas as pd
data = pd.read_csv('data.csv')

print(data.isnull().sum()) # Проверяем наличие пропусков

data['Score'].fillna(data['Score'].mean(), inplace=True) # Заполняем пропуски в столбце 'Score' средним значением

data.dropna(subset=['Group'], inplace=True) # Удаляем строки с пропусками в столбце 'Group'
data.to_csv('cleaned_data.csv', index=False)