# Import csv module
import csv

# We now do the same for csv files. We create a csv file with content and read its content.

with open("names.csv" , "w" , newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["Male" , "Female"]) # specify what is in the 1st row
    writer.writerow(["James" , "Joy"])  # specify whats in the second row


# SECOND METHOD OF WRITING IN CSV USING DictWriter

with open("marks.csv" , "w") as file:
    writer = csv.DictWriter(file , fieldnames=["Name" , "Marks"])
    writer.writerow({"Name" : "James" , "Marks" : "70" , "Name" : "Joy" , "Marks" : "80" })

# With using the DictWriter the field names dont appear in the csv file. Its only thr vslues.


# We now read the content in those csv files

with open("names.csv" , "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("marks.csv" , "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)