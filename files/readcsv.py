import csv
file=open("student_records.csv","r")
reader = csv.reader(file,delimiter=" ")
for row in reader:
    rowlist=row
    for columb in rowlist:
        print(columb)
    