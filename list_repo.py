from secrets import API_URL, OWNER
from pprint import pprint
import requests
import urllib

queryParam = {'page': 1, 'per_page': 100}
queryString = urllib.parse.urlencode(queryParam)

headers = {
    "Accpet": "application/vnd.github.v3+json"
}

try:
    # print(API_URL + "/users/" + OWNER + "/repos")
    req = requests.get(API_URL + "/users/" + OWNER +
                       "/repos?" + queryString, headers=headers)
    req.raise_for_status()

    repos = req.json()

    for repo in repos:
        print(repo["full_name"])
except requests.exceptions.RequestException as err:
    raise SystemError(err)
