import git
import os

def git_init_commit_push(local_path, commit_message="Initial commit via Streamlit app", remote_url=None):
    """
    Initialize a git repo, add files, commit, and push to remote.

    Args:
        local_path (str): Local folder path
        commit_message (str): Commit message
        remote_url (str): GitHub repo URL to push (optional if already set)
    """
    try:
        repo = git.Repo.init(local_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)

        if remote_url:
            origin = None
            if 'origin' in repo.remotes:
                origin = repo.remotes.origin
                origin.set_url(remote_url)
            else:
                origin = repo.create_remote('origin', remote_url)
            origin.push(refspec='master:master')

        return True, "Files committed and pushed successfully!"
    except Exception as e:
        return False, str(e)
