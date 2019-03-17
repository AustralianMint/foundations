##Finds Given color in CSV file
#Returns I love that color too
import csv
fav_color = str(input("Enter your fav color: "))

#opening csv (in r mode cause of Dictionary)and renaming to 'csv_file'
with open('colors.csv', mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if row["realName"] != fav_color:
            print(row["realName"])
            line_count += 1
        else:
            print("I love {} too!".format(row["realName"]))
