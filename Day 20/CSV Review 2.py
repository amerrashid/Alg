import csv

row_count = 0
biostats_info = [["Name", "Sex", "Age", "Height (cm)", "Weight(kg)"]]

with open("biostats.csv") as in_file:

    reader = csv.reader(in_file)
    next(reader)
    for row in reader:
        row[3] = round(float(row[3])*2.54)
        row[4] = round(float(row[4])*0.454)
        biostats_info.append(row)
        #row_count += 1


    with open("stats.csv", 'w', newline='') as out_file:

        writer = csv.writer(out_file)
        writer.writerows (biostats_info)

