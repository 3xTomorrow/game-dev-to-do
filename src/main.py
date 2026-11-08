# Runs GUI here
import os.path
from git_runner import *

def main():
    with open("data/PAT.txt") as f:
        if os.path.getsize("data/PAT.txt") == 0:
            pat = input("GitHub Personal Access Token: ")
            f.write(pat)
        else:
            pat = f.readline()[3:]

        github = authenticate(pat)
        if github:
            repo_contents = get_repo_contents(github,"3xTomorrow","Late-Night-Deadline")
            print(repo_contents)
        else:
            print("Not a valid GitHub Personal Access Token")

if __name__ == "__main__":
    main()