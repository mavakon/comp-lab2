import pandas as pd
import matplotlib.pyplot as plt

# Зчитування датасету з файлу .txt, де дані розділені пробілами
data = pd.read_csv("DS5.txt", sep=' ', header=None, names=['x', 'y'])

# Створення фігури з розміром полотна 960x540 пікселів
fig = plt.figure(figsize=(960/100, 540/100)) 

# Встановлення осей графіка, щоб вони займали весь простір фігури
ax = fig.add_axes([0, 0, 1, 1])  # [лівий край, нижній край, ширина, висота]

# Розташування точок
ax.scatter(data['x'], data['y'])

# Збереження результату у файл
plt.savefig("output.png", dpi=100)

# Відображення полотна у вікні
plt.show()
