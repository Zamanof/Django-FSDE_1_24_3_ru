import requests

# response = requests.get("http://localhost:5093/api/Products")
# data = response.json()
# print(data)

def github_repo_demo():
    response = requests.get("https://api.github.com/repos/Zamanof/Django-FSDE_1_24_3_ru", timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"Repo {data["full_name"]}")
    print(f"URL: {data['html_url']}")

github_repo_demo()