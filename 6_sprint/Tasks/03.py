# In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],
#
# in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...].
#
# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:
#
# header line - user, department
#
# next lines :  <userName>, <departmentName>
#
# If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.
#
# Create appropriate json-schemas for user and department.
#
# If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception
#
# To validate instances create function validate_json(data, schema)

import json
import jsonschema
from jsonschema import validate
import csv


class DepartmentName(Exception):
    pass


class InvalidInstanceError(Exception):
    pass


def user_with_department(csv_file, user_json, department_json):
    user_schema = {
        "type": "object",
        "required": ["name", "department_id"],
        "properties": {
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        }
    }

    department_schema = {
        "type": "object",
        "required": ["id", "name"],
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        }
    }

    def is_valid(data, schema, schema_name):
        try:
            validate(data, schema)
        except jsonschema.exceptions.ValidationError:
            raise InvalidInstanceError(f"Error in {schema_name} schema")
        return True

    def get_valid(file, schema, schema_name):
        with open(file) as json_file:
            return [elem for elem in json.load(json_file) if is_valid(elem, schema, schema_name)]

    personal = []
    for user in get_valid(user_json, user_schema, "user"):
        find_department = False
        for department in get_valid(department_json, department_schema, "department"):
            if user.get("department_id") == department.get("id"):
                personal.append({"name": user.get("name"), "department": department.get("name")})
                find_department = True
        if not find_department:
            raise DepartmentName(f"Department with id {user.get('department_id')} doesn't exists")

    # print(personal)
    fields = ['name', 'department']

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(personal)


# print(read_from_json("user.json"))
# print(get_valid("user.json", user_schema))
# print(is_valid("user.json", user_schema))
#
# print(get_valid("department.json", department_schema))
# print(is_valid("department.json", department_schema))

# user_with_department("csv_result.csv", "user.json", "department.json")
# user_with_department("user_department.csv", "user_without_dep.json", "department.json")

# try:
#     user_with_department("user_department.csv", "user_without_dep.json", "department.json")
# except DepartmentName as e:
#     print(str(e))

# user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")

try:
    user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
except InvalidInstanceError as e:
    print(str(e))