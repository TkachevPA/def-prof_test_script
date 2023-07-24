import pandas as pd

file_name = 'input/Таблица.xlsx'  # путь к входным данным

data = pd.read_excel(file_name) # чтение файла в набор данных
data = data.fillna(0) # заполнение нулями пустых ячеек
data.to_pickle('data')

print(data)
