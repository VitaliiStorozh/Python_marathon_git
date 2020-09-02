# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords.
#
# Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.
#
# Examples:
# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
# mary.lastname ➞ "Major"
# richard.height ➞ 178
# giancarlo.nationality ➞ "Italian"
# john.name ➞ "John"

class Employee():
    def __init__(self,fullname, **kwargs):
        self.name = fullname.split(" ")[0]
        self.lastname = fullname.split(" ")[1]
        self.__dict__.update(kwargs)

john = Employee('John Doe')
print(john.lastname)

mary = Employee('Mary Major', salary=120000)
print(mary.salary)

richard = Employee('Richard Roe', salary=110000, height=178)
print(richard.salary)
print(richard.height)

giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)

peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(peng.subordinates)