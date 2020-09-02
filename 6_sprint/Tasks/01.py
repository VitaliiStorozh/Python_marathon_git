# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.
# import json

# data1 = [{"name": "user_1", "password": "pass_1"},
#          {"name": "user_2", "password": ["pass_1", "qwerty"]}]
# # find("1.json", "password") returns ["pass_1", "qwerty"]
#
# data2 = [{"name": "user_1", "credentials": {"username": "user_user", "password": "1234qweQWE"}},
#          {"name": "user_2", "password": ["pass_1 ", "qwerty "]}]
# # find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
#
# data3 = {"name": "user_1", "credentials": {"username": "user_user", "password": "1234qweQWE"}}
# # find("3.json", "password") returns ["1234qweQWE"]
#
# with open("data_1", "w") as write_file:
#     json.dump(data1, write_file)
# with open("data_2", "w") as write_file:
#     json.dump(data2, write_file)
# with open("data_3", "w") as write_file:
#     json.dump(data3, write_file)

def find(file, key):
    import json
    with open(file) as read_file:
        data = json.load(read_file)
    values = set()


    def parse2(o):
        if type(o) == list:
            for item in o:
                return parse2(item)
        if type(o) == dict:
            return parseObj(o)

    def parseObj(obj):
        """Може повертати обєкт або ліст"""
        if obj.get(key) is not None:
            return obj.get(key)
        elif obj.get("credentials") is not None:
            return obj.get("credentials").get(key)
        else:
            return None

    if type(data) == list:
        for item in data:
            parseResult = parseObj(item)
            if parseResult is None:
                continue
            if type(parseResult) == list:
                for object in parseResult:
                    values.add(object)
            else:
                values.add(parseResult)

    else:
        parseData = parseObj(data)
        if parseData is not None:
            if type(parseData) is list:
                for item in parseData:
                    values.add(item)
            else:
                values.add(parseData)

    return list(values)


print(find("data_1", "password"))
print(find("empty", "password"))
print(find("data_2", "password"))
print(find("data_3", "password"))
