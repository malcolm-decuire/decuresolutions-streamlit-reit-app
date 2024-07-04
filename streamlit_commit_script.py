import os
import git

# Variables
REPO_URL = "https://github.com/malcolm-decuire/decuresolutions-streamlit-reit-app.git"
CLONE_DIR = "decuresolutions-streamlit-reit-app"
COMMIT_MESSAGE = "Early Morning Trappin"

# Clone the repository
if not os.path.exists(CLONE_DIR):
    git.Repo.clone_from(REPO_URL, CLONE_DIR)

# Change to the repository directory
repo = git.Repo(CLONE_DIR)
assert not repo.bare

# Make changes here (this is an example, replace it with your actual changes)
with open(os.path.join(CLONE_DIR, "README.md"), "a") as readme_file:
    readme_file.write("# Temporary change\n")

# Stage all changes
repo.git.add(A=True)

# Commit the changes
repo.index.commit(COMMIT_MESSAGE)

# Push the changes
origin = repo.remote(name='origin')
origin.push()

# Clean up (optional)
# import shutil
# shutil.rmtree(CLONE_DIR)
