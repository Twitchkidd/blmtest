import json
import subprocess
import requests
import sys


def main():
    with open("./repo.txt", 'r') as repoF:
        tokenRepoScope = repoF.read(40)
    gbmm = subprocess.Popen(
        ["git", "branch", "-m", "master", "main"], shell=True, stdout=subprocess.PIPE)
    # gpom = subprocess.Popen(["git", "push", "-u", "origin", "master"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gpom = subprocess.Popen(
        ["git", "push", "-u", "origin", "main"], shell=True, stdout=subprocess.PIPE)
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
            f"Default branch for dep-server updated to main!")
    subprocess.Popen(["git", "push", "--delete", "origin",
                      "main"], shell=True, stdout=subprocess.PIPE)
    sys.exit()


if __name__ == "__main__":
    main()
