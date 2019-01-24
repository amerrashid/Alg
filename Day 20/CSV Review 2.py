import csv

row_count = 0
height = 0
weight = 0

with open("biostats.csv") as in_file:


    with open("stats.csv", 'w', newline='') as out_file:

        reader = csv.reader(in_file)
        writer = csv.writer(out_file)
        for x in reader:

            writer.writerow(in_file)

