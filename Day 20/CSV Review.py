import csv

row_count = 0
female_count = 0
total_age = 0
average_age = 0
female_percentage = 0

with open("biostats.csv") as csv_file:
    reader = csv.reader (csv_file)

    next(reader)

    for row in reader:

        total_age += float(row[2])
        row_count += 1

        if row[1] == "F":
            female_count += 1

    female_percentage = ((female_count)/(row_count)) * 100

average_age = total_age / (row_count)

print(total_age)
print(row_count)
print ("Average age of all respondents: {:0.2f}".format(average_age))
print ("The Percentage of Females in the set: {:0.2f}".format(female_percentage))
