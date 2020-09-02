# In case  we need to get information about different entities in the json-format
# that are returned as a result of a request to the server.
# Create a get_request(url) function returns a lambda function that receives url parameters as keyword arguments.
# This lambda function should return json object.

import requests

def get_request(url):
    return lambda **kwargs: requests.get(url, params=kwargs).json()

comments = get_request("https://jsonplaceholder.typicode.com/comments")
print(comments(postId=1, email='Lew@alysha.tv'))