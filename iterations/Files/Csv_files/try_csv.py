# Import the necessary modules 
from pathlib import Path
import csv

# Specify the folder

folder = Path(r"C:\Users\Kxbuga\Desktop\python-concepts\iterations\Files\Csv_files")

# Specify the file

file_path = folder / "names.csv"

# make sure that the folder exists

folder.mkdir(parents = "TRUE" , exist_ok = True)

# use the open method

with open(file_path , "w" , newline = "") as file:
    # create a writer
    writer = csv.writer(file)
    # now write individual rows
    gender = writer.writerow(['MALE' , 'FEMALE'])
    # WRITE SECOND ROW
    names = writer.writerow(['James' , 'Joy'])


# SECOND METHOD OF WRITING INSIDE OUR FILE USING A DICT WRITER

# A dictwriter doesnt include the field names in our csv files

# We try create another file that takes the name and the marks. Column one name and Column two marks


folder_2 = Path(r"C:\Users\Kxbuga\Desktop\python-concepts\iterations\Files\Csv_files")

# Specify the file

file_path2 = folder_2 / "marks.csv"

# make sure that the folder exists

folder_2.mkdir(parents = True , exist_ok = True)

# Use open method

with open(file_path2 , "w" , newline="") as file:
    # create a dict writer

    writer = csv.DictWriter(file , fieldnames = ["Name" , "Marks" ])

    # now use our writer to write the rows

    writer.writerows([
        {"Name": "James", "Marks": 70},
        {"Name": "Joy", "Marks": 60}
    ])

    # now read our content inside the file


with open(file_path2  , "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
