import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/perm.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """Получение дат, температурных минимумов и максимумов из файла"""