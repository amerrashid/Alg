import csv

csv_data = [["Student ID", "Grade"], ["123312", "A"]]


with open('person.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)