from role_normalizer import normalize_role
import requests
import json

URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

PARAMS = {
    "app_id": "dad4df96",
    "app_key": "773246c9d5b50e31eaf8d66151785d04",
    "results_per_page": 10000,
}

response = requests.get(URL, params=PARAMS)

data = response.json()
for job in data["results"]:
    title = job.get("title", "")
    role = normalize_role(title)

    if role:
        print({
            "raw_title": title,
            "normalized_role": role
        })
