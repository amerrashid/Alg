import csv

person = [["Student ID", "Grade"], ["123312", "A"]]

csv.register_dialect ('myDialect', quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True, lineterminator= "\n")

with open('person.csv', 'w') as f:
    writer = csv.writer(f, dialect= 'myDialect')
    for row in person:
        writer.writerow(row)