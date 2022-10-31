# Dictionaries


steve = {
    "name" : "Steve",
    "weight" : 155.5,
    "height" : 70,
    "foods" : ["country fried steak", "fried chicken", "collards"],
    "ice cream":{
        "vanilla":False,
        "chocolate":True,
        "coffee":False,
    },
    10 : "this has an integer key"
}

# name_of_dict[KEY]

#for key in steve.values:
print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items())
for key, value in steve.items():
    if isinstance(value, list):
        print(f"The list is at {key}")

