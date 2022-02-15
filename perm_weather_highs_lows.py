import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/perm.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """Чтение дат и максимальных температур из файла"""
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[2])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

"""Нанесение данных на диаграмму"""
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

"""Форматирование диаграммы"""
plt.title("Высшая и низшая дневная температура - 2022", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Температура (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
