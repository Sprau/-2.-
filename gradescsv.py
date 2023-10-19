import csv

import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="grades.csv")

grades = []
newGrades = []

with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        grades.append(dict(zip(header, row)))
for i in grades:
    summ = 0
    newData = {}
    for j in i:
        i[j] = i[j].replace(' ', '').replace('"', '')
        print(j, ' ', i[j])
        if 'Test' in j or 'Final' in j:
            summ += float(i[j])
        else:
            newData[j.replace(' ', '').replace('"', '')] = i[j]

    avg = summ / 5
    newData['avg'] = avg
    newGrades.append(newData)


mixGrades = {
    'A+': 90,
    'A': 85,
    'A-': 80,
    'B+': 75,
    'B': 70,
    'B-': 65,
    'C+': 60,
    'C': 55,
    'C-': 50,
    'D+': 45,
    'D': 40,
    'D-': 35,
    'E': 30,
    'F': 0
}


print(newGrades)
