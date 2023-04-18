import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/datasets.csv'
data = pd.read_csv(url)
data = data.dropna() # удаляем строки с пропущенными значениями
data = data.loc[(data['Cols'] >= 10) & (data['Rows'] >= 500)] # выбираем датасеты с не менее 10 признаками и не менее 500 записями
data = data.sample() # выбираем случайный датасет из отфильтрованных
print(data['Package'].values[0], data['Item'].values[0])

data_url = data['CSV'].values[0]
data = pd.read_csv(data_url)
print('Многомерность данных:', len(data.shape) > 1)
print(data.describe())
sns.pairplot(data)
plt.show()

print(data.head())
print(data.tail())

print(data.info())

print(data.isnull().sum())