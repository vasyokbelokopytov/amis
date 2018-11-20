def print_name(dataset):
    if len(dataset) == 0:
        return
    name = (dataset[0])["student"]["name"]
    print(name)
    print_name(dataset[1:])


def find_student(dataset, name_of_teacher):
    name_of_students = []
    for element in dataset:
        for lab in element["labs"]:
            if element['labs'][lab]["teacher"] == name_of_teacher:
                name_of_students.append(element["student"]["name"])

    return name_of_students


dataset = [
    {
        "student": {
            "name": "Vasya"
        },
        "labs": {
            "first": {
                "name": "first",
                "mark": 5,
                "teacher": "Bob"
            },
            "second": {
                "name": "second",
                "mark": 6,
                "teacher": "Boba"
            }
        }
    },
    {
        "student": {
            "name": "Petya"
        },
        "labs": {
            "first": {
                "name": "first",
                "mark": 5,
                "teacher": "Bob"
            }
        }
    }
]
print_name(dataset)
print(find_student(dataset, "Bob"))
