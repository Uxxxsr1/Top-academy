%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Читаем CSV файл
df = pd.read_csv('bd.csv')

# Создаем график
plt.figure(figsize=(12, 7))

# График продаж
plt.plot(df['Month'], df['Sales'], 'o-', linewidth=3, markersize=8, label='Продажи', color='blue')

# График расходов
plt.plot(df['Month'], df['Expenses'], 's--', linewidth=3, markersize=8, label='Расходы', color='red')

# Настраиваем внешний вид
plt.title('Динамика продаж и расходов', fontsize=16, fontweight='bold')
plt.xlabel('Месяц', fontsize=14)
plt.ylabel('Сумма ($)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xticks(rotation=45)

# Добавляем аннотации
for i, (sales, expenses) in enumerate(zip(df['Sales'], df['Expenses'])):
    plt.annotate(f'{sales}', (i, sales), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{expenses}', (i, expenses), textcoords="offset points", xytext=(0,-15), ha='center')

plt.tight_layout()
plt.show()