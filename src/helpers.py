"""
The file contains all the necessary helper functions, that will be needed in different stages of project.
"""
# Imports
import requests
import json

## Function to extract data from a url's that serve json data in a json-format.
def _get_json_(url, headers={}, params={}):
    session = requests.session()
    print("Fetching - {0}".format(url))
    response = session.get(
        url=url,
        headers=headers,
        params=params
    ).text
    json_data = json.loads(response)
    return json_data


if __name__ == "__main__":
    print(_get_json_())