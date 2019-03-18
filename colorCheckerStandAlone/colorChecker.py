##Runs through given CSV file and prints out all collumns with their value.
import csv
fav_color = str(input("Enter your fav color: "))

#opening csv and renaming to 'csv_file'
with open('colors.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    #Looping throug entre CSV file
    for row in csv_reader:
        if line_count == 0:
            print(", ".join(row))
            line_count += 1
        else:
            print("NAME1: {}, NAME2: {}, NAME3: {}".format(row[0], row[1], row[3]))
            line_count += 1

    #End with totat lines printed.
    print("{} lines printed.".format(line_count))
