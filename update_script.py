import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")
repo_url = "https://github.com/your-username/your-repo.git"

g = Github(github_token)
repo = g.get_repo("your-username/your-repo")

# Pull the latest changes
os.system("git pull " + repo_url)
