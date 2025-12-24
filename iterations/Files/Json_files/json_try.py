# import the necessary modules

from pathlib import Path
import json

# specify the folder

folder = Path(r"C:\Users\Kxbuga\Desktop\python-concepts\iterations\Files\Json_files")

# specify the file location with its name

file_path = folder / "details.json"

# check if the folder exists. Good practise ensures we prevent future conflicts

try:
    folder.mkdir(parents = True , exist_Ok = True)
except:
    print("Missing directory")


# since we dont have our data we create the data and store it in a dictiionary. JSON works well with this

data = {
    "Name" : "James" ,
    "Age" : 20 ,
    "Skills" : "Python, SQL , Javascript" 
}

# now use our open method

with open(file_path , "w") as file:
    # dump our data into json
    json.dump(data , file , indent = 4)


# now read the data in our json file

with open(file_path , "r") as file:
    content = json.load(file)
    for indx , item in enumerate(content.values() , start = 1):
        print(f"{indx}.{item}")

    # for indx , item in enumerate(content.items() , start = 1):
    #     print(f"{indx}.{item}")

# Just play around with .items() and .values() depending on what we want to display.