import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def random_num(first, last):
    return round(random.uniform(first, last), 0)

def random_float(first, last):
    return round(random.uniform(first, last), 1)

def random_category(first, last):
    return "Category " + str(round(random.uniform(first, last), 0))

def write_to_csv(file_name, column_header, rowNumber):
    with open(file_name, mode='w', newline = '') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(column_header)
        for i in range(rowNumber):
            correct_answer = random_num(0, 10)
            answer_time = random_float(130,140)
            row = [correct_answer, answer_time]
            writer.writerow(row)

column_header = ['CorrectAnswer', 'AnswerTime']

rowNumber = 10

write_to_csv('test.csv',column_header,rowNumber)


data = pd.read_csv('data.csv')
# Plot raw data
plt.scatter(data['CorrectAnswer'],data['AnswerTime'])

plt.show()