import json
from subprocess import Popen, PIPE
import requests
import sys


def main():
    with open("./repo.txt", 'r') as repoF:
        tokenRepoScope = repoF.read(40)
    gbmm = subprocess.Popen(
        ["git", "branch", "-m", "master", "main"], shell=True, stdout=PIPE, stderr=PIPE).wait()
    gpom = subprocess.Popen(
        ["git", "push", "-u", "origin", "master"], shell=True, stdout=PIPE, stderr=PIPE).wait()
    url = "https://api.github.com/repos/Twitchkidd/test"
    params = json.dumps({"default_branch": "main"})
    headers = {"Authorization": 'token ' + tokenRepoScope}
    patchDefaultResponse = requests.patch(url, data=params, headers=headers)
    if patchDefaultResponse.status_code >= 400:
        print(
            f"Network error! Status code: {patchDefaultResponse.status_code} {patchDefaultResponse.json()}")
        sys.exit()
    else:
        print(
            f"Default branch for test updated to main!")
    gpom = subprocess.Popen(
        ["git", "push", "--delete", "origin", "master"], shell=True, stdout=PIPE, stderr=PIPE).wait()
    sys.exit()


if __name__ == "__main__":
    main()
