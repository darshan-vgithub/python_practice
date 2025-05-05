marks = {
    "harry": 99,
    "rohan": 98,
    "shubham": 97,
    "girls": {
        "priya": {
            "maths": 99,
            "science": 98
        },
        "priyanka": {
            "maths": 99,
            "science": 98
        }
    },
    "taecher":["purushottam","sudhanshu"]
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":100,0:0})
print(marks)

print(marks.get("harry")) # it will return the value of the key if the key is present else it will return none
print(marks["harry"]) # it will throw an error if the key is not present

