import csv
with open ("test.csv") as csvfile:
    reader = csv.reader (csvfile)
    next(reader)
    for row in reader:
        print (row)