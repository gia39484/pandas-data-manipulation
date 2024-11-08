import pandas as pd
data1 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print('max', data1.max())
print('median', data1.median())
print('sum', data1.sum())
print('min', data1.min())
print('mean', data1.mean())
data2 = data1*2
print(data2)
print('===============')
data = pd.DataFrame({
    'name': ['Amy', 'John', 'Bob', 'emily', 'chris', 'steven', 'josh', 'joe'],
    'salary': [60_000, 50_000, 70_000, 43_000, 67_000, 33_000, 63_000, 81_000]
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print('薪資表', data['salary'], sep='\n')
print('第三列', data.iloc[2], sep='\n')
print('員工資料表', data)
print('資料數量', data.size)
print('資料型式（列,欄）', data.shape)
print('資料索引', data.index)
print('取得第一列資料(索引)', data.loc['a'], sep='\n')
names = data['name']
print('轉大寫', names.str.upper(), sep='\n')
salaries = data['salary']
print('平均新水', salaries.mean())
data['revenue'] = [500_000, 600_000, 700_000, 990_000, 369_000, 901_000, 870_000, 235_000]
data['age'] = pd.Series([33, 26, 28, 45, 21, 28, 34, 30], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
data['contribution'] = data['revenue']/data['salary']
print('員工新增後資料表', data, sep='\n')
max_con = round(data['contribution'], 2)
print('最高貢獻值', max_con.max())