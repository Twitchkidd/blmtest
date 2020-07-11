import json
from subprocess import Popen, PIPE
import requests
import sys


def main():
    with open("./repo.txt", 'r') as repoF:
        tokenRepoScope = repoF.read(40)
    gbmm = Popen(
        ["git", "branch", "-m", "main", "master"], stdout=PIPE, stderr=PIPE)
    gbmmStdout, gbmmStderr = gbmm.communicate()
    gpom = Popen(
        ["git", "push", "-u", "origin", "master"], stdout=PIPE, stderr=PIPE)
    gpomStdout, gpomStderr = gpom.communicate()
    url = "https://api.github.com/repos/Twitchkidd/test"
    params = json.dumps({"default_branch": "master"})
    headers = {"Authorization": 'token ' + tokenRepoScope}
    patchDefaultResponse = requests.patch(url, data=params, headers=headers)
    if patchDefaultResponse.status_code >= 400:
        print(
            f"Network error! Status code: {patchDefaultResponse.status_code} {patchDefaultResponse.json()}")
        sys.exit()
    else:
        print(
            f"Default branch for test updated to master!")
    gpd = Popen(
        ["git", "push", "--delete", "origin", "main"], stdout=PIPE, stderr=PIPE)
    gpdStdout, gpdStderr = gpd.communicate()
    sys.exit()


if __name__ == "__main__":
    main()
