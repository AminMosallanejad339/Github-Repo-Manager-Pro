import streamlit as st
import os
from pathlib import Path
from utils.github_utils import create_github_repo, delete_github_repo
from utils.git_utils import git_init_commit_push

# Configure Streamlit page
st.set_page_config(page_title="GitHub Repo Manager", layout="wide")

st.title("GitHub Repository Manager")
st.write("Create, push, and delete GitHub repositories directly from your local system.")

# -------------------------------
# User credentials
# -------------------------------
username = st.text_input("GitHub Username")
token = st.text_input("Personal Access Token", type="password")

# -------------------------------
# Repository actions
# -------------------------------
action = st.radio("Select action:", ["Create Repo", "Delete Repo"])
repo_name = st.text_input("Repository Name")

# -------------------------------
# Folder selection (only for create)
# -------------------------------
folder_path_input = st.text_input(
    "Local folder path (e.g., /mnt/e/Proj/Github-Repo-Manager-Pro/examples/sample_folder)"
)

folder_path = Path(folder_path_input.strip()) if folder_path_input else None

# -------------------------------
# Create Repository
# -------------------------------
if action == "Create Repo" and st.button("Create and Push"):
    if not all([username, token, repo_name, folder_path_input]):
        st.error("Please fill all fields!")
    elif not folder_path.exists():
        st.error(f"Folder path does not exist:\n{folder_path}")
    else:
        success, msg = create_github_repo(username, token, repo_name, private=True)
        st.info(msg)
        if success:
            remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
            git_success, git_msg = git_init_commit_push(str(folder_path), remote_url=remote_url)
            if git_success:
                st.success(git_msg)
            else:
                st.error(git_msg)

# -------------------------------
# Delete Repository
# -------------------------------
if action == "Delete Repo" and st.button("Delete Repository"):
    if not all([username, token, repo_name]):
        st.error("Please fill all fields!")
    else:
        success, msg = delete_github_repo(username, token, repo_name)
        if success:
            st.success(msg)
        else:
            st.error(msg)
