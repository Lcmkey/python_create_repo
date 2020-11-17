import os
import argparse
from secrets import WHOAMI, GITHUB_TOKEN, API_URL, OWNER
from pprint import pprint
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private

# print(args)

if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

print(payload)

headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accpet": "application/vnd.github.v3+json"
}

try:
    req = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
    req.raise_for_status()

    pprint(req.json())
except requests.exceptions.RequestException as err:
    raise SystemError(err)


try:
    REPO_PATH = "/home/" + WHOAMI + "/Desktop/github/"
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPO_PATH + repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/" + OWNER + "/" +
              repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system(
        "git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
    raise SystemError(err)

# req = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
