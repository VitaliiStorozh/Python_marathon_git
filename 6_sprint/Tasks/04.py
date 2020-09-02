# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
#
# Make both classes JSON serializable.
#
# Json-files represent information about student (students).
#
# Create methods:
#
# Student.from_json(json_file) that return Student instance from attributes from json-file;
#
# Group.serialize_to_json(list_of_groups, filename)
#
# Group.create_group_from_file(students_file)
#
# Parse given files, create instances of Student class and create instances
# of Group class (title for group is name of json-file without extension).

import json
import os


class Student:

    def __init__(self, full_name:str, avg_rank: float, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, file):
        with open(file) as read_file:
            data = json.load(read_file)
            return Student.create_from_dict(data)

    @classmethod
    def create_from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return self.full_name + " (" + str(self.avg_rank) + "): " + str(self.courses)


class Group:

    def __init__(self, title, students):
        self.title = title
        self.students = students

    @classmethod
    def create_group_from_file(cls, file):
        with open(file) as read_file:
            data = json.load(read_file)
            title = os.path.splitext(file)[0]
            students = []
            if type(data) == dict:
                students.append(Student(**data))
            elif type(data) == list:
                for student in data:
                    students.append(Student.create_from_dict(student))
            return Group(title, students)

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        with open(filename, 'w') as outfile:
            json.dump(list_of_groups, outfile, default=lambda o:o.__dict__, indent=4)

    def __str__(self):
        return self.title + ": [" + ', '.join(['"' + str(elem) + '"' for elem in self.students]) + "]"


# with open("2020_2.json") as read_file:
#     user2 = json.load(read_file)
# print([str(Student(**item)) for item in user2])



user1 = Student.from_json("2020-01.json")
print(user1)

g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2], "g2.json")
