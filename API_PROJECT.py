import requests
def get_git_user_data(username):
    url=f"https://api.github.com/users/{username}"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        return None