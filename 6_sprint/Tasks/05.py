# Create context manager class SerializeManager with attributes filename and type for serializing python object to
# different formats.
# For defining format create enum FileType with values JSON, BYTE. Create function serialize(
# object, filename, fileType).
# This function should serialize object to filename according to type.
# For example:
# if user_dict = { 'name': 'Roman', 'id': 8}
# then
# serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2"
# and this file will contain user_dict as byte array serialize("String", "string.json", FileType.JSON) ->
# creates file with name "string.json" and text "String"

import json
import pickle
from enum import Enum


class FileType(Enum):
    JSON = "w"
    BYTE = "wb"


class SerializeManager:

    def __init__(self, file_name, type: FileType):
        self.filename = file_name
        self.type = type
        self.file_object = open(file_name, type.value)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file_object.close()

    def serialize(self, obj2):
        if self.type == FileType.JSON:
            json.dump(obj2, self.file_object)
        elif self.type == FileType.BYTE:
            pickle.dump(obj2, self.file_object)


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)
