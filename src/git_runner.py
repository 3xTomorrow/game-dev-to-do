from github import Github
from github import Auth

def authenticate(PAT: str):
    return Github(auth=Auth.Token(PAT))

def get_repo_contents(github, owner_name: str, repo_name: str) -> list:
    repo = github.get_repo(owner_name + "/" + repo_name)
    return repo.get_contents("")