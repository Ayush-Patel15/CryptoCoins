import requests
import json

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