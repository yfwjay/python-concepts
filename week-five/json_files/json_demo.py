import json

# We do the same for JSON files.
# We write and read files of .json

# TO WRITE A FILE.

# We define the data

data = {
    "Name" : "James" ,
    "Age" : 19 ,
    "Skills" : ['Python' , "MYSQL" ]
}

with open("intro.json" , "w") as file:
    json.dump(data , file , indent = 4)

# We read the data in our file intro.json

with open("intro.json" , "r") as file:
    content = json.load(file)
    print(content)