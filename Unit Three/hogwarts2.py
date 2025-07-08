students = {
    "Hermionie": "Griffindor" ,
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep="--> ")

students = [
    {"name":"Hermionie", "house": "Griffindor" , "patronous": "Otter"},
    {"name":"Harry", "house": "Griffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronous": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None},
]

for student in students:
    print(student["name"], students["house"], sep="--> ")