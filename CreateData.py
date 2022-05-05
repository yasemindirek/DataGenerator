import csv
import random

def random_float(first, last):
    return round(random.uniform(first, last), 0)

def random_category(first, last):
    return "Category " + str(round(random.uniform(first, last), 0))

def write_to_csv(file_name, column_header, rowNumber):
    with open(file_name, mode='w', newline = '') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(column_header)
        for i in range(rowNumber):
            correct_answer = random_float(201, 300)
            answer_time = random_float(0, 20)
            row = [correct_answer, answer_time]
            writer.writerow(row)

column_header = ['CorrectAnswer', 'AnswerTime']

rowNumber = 500

write_to_csv('data.csv',column_header,rowNumber)