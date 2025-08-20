from github import Github, GithubException

def create_github_repo(username, token, repo_name, private=True, description="Created via Streamlit app"):
    try:
        g = Github(token)
        user = g.get_user()
        repo = user.create_repo(
            name=repo_name,
            private=private,
            description=description,
            auto_init=False
        )
        return True, f"Repository '{repo_name}' created successfully!"
    except GithubException as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def delete_github_repo(username, token, repo_name):
    try:
        g = Github(token)
        user = g.get_user()
        repo = user.get_repo(repo_name)
        repo.delete()
        return True, f"Repository '{repo_name}' deleted successfully!"
    except GithubException as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)
