import os
from git import Repo
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")
repo_path = "/path/to/your/local/repo"  # Update with the path to your local repository

def upload_to_github():
    try:
        # Open the local repository
        repo = Repo(repo_path)

        # Check if there are any changes
        if repo.is_dirty(untracked_files=True):
            # Add all changes to the index
            repo.git.add("--all")

            # Commit the changes
            repo.index.commit("Automated commit for server update")

            # Push changes to GitHub
            repo.remotes.origin.push()

            print("Code successfully pushed to GitHub.")
        else:
            print("No changes to push.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    upload_to_github()
