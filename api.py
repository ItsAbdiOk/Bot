import requests
import json

base_url = "https://api.mangadex.org"
title = "The Greatest Estate Devloper"

# Fetch manga ID
response = requests.get(f"{base_url}/manga", params={"title": title})
manga_id = response.json()["data"][0]["id"]
print(f"The Manga's ID is {manga_id}")

# Fetch manga chapters
response = requests.get(f"{base_url}/manga/{manga_id}/aggregate")
api_chapters = response.json()

# Store the data in a JSON file
with open("data.json", "w") as f:
    json.dump(api_chapters, f, indent=4)

# Parse API response from file
with open("data.json", "r") as f:
    data = json.load(f)

# Extract chapters from all volumes
chapters = []
for volume_data in data["volumes"].values():
    chapters.extend(volume_data["chapters"].keys())

# Find highest chapter number
highest_chapter = max(map(int, chapters))

print(highest_chapter)  # Output: highest chapter number
