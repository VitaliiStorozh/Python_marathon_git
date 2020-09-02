# Define a class Employee. In the class Employee, implement the instance attributes as firstname, lastname and salary.
#
# Create the method from_string() which parses a string containing these attributes and
# assigns them to the correct properties. Properties will be separated by a dash.
#
# Examples:
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
# emp1.firstname ➞ "Mary"
# emp1.salary ➞ 60000
# emp2.firstname ➞ "John"

class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)
    @classmethod
    def from_string(cls, str):
        return cls(str.split("-")[0], str.split("-")[1], int(str.split("-")[2]))

emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)

emp3 = Employee.from_string("Susan-Walker-70000")
print(emp3.firstname)
print(emp3.lastname)
print(emp3.salary)

emp4 = Employee.from_string("Michael-Ferry-90000")
print(emp4.firstname)
print(emp4.lastname)
print(emp4.salary)

emp5 = Employee("Graham", "Derrell", 55000)
print(emp5.firstname)
print(emp5.lastname)
print(emp5.salary)