import subprocess
import requests

with open("./repo.txt", 'r') as repoF:
    tokenRepoScope = repoF.read(40)
subprocess.Popen(["git", "branch", "-m", "main", "master"])
subprocess.Popen(["git", "push", "-u", "origin", "master"])


def constructPatchDefaultUrl(repo):
    return f"{GITHUB_API}/repos/{repo['owner-login']}/{repo['name']}"


url = "https://api.github.com/repos/Twitchkidd/test"
params = json.dumps({"default_branch": "master"})
headers = {"Authorization": 'token ' + tokenRepoScope}
patchDefaultResponse = requests.patch(url, data=params, headers=headers)
if patchDefaultResponse.status_code >= 400:
    logging.warning(f"Response status: {patchDefaultResponse.status_code}")
    print(
        f"Network error! Status code: {patchDefaultResponse.status_code} {patchDefaultResponse.json()}")
else:
    print(
        f"Default branch for dep-server updated to main!")
subprocess.Popen(["git", "push", "--delete", "origin", "main"])
