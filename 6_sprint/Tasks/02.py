import json

# Implement function parse_user(output_file, *input_files)
# for creating file that will contain only unique records (unique by key "name") by merging information
# from all input_files argument (if we find user with already existing name from previous file we should ignore it).
#
#
# If the function cannot find input files we need to log information with error level
#
# root - ERROR - File <file name> doesn't exists
#
# For example:
# user1_json = [{"name": "Bob1", "rate": 1, "languages": ["English"]},
#               {"name": "Bob2", "rate": 0.78, "languages": ["English", "French"]}
#               ]
#
# user2_json = [{"name": "Bob1", "rate": 25, "languages": ["French"]},
#               {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
#               ]

# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]
# with open("user3.json", "w") as write_file:
#     json.dump(user3_json, write_file)

import json
import logging
import os

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    import json
    output_dict = {}
    for file in input_files:
        if not os.path.exists(file):
            logging.error(f"File {file} doesn't exists")
            continue
        with open(file) as read_file:
            data = json.load(read_file)

        for item in data:
            name = item.get("name")
            if name is not None and name not in output_dict:
                output_dict[name] = item

    with open(output_file, "w") as write_file:
            json.dump(list(output_dict.values()), write_file, indent=4)

parse_user("user4.json", "user1.json", "user2.json")
# print_file("user4.json")