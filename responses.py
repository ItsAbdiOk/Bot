import random
import requests
import json

def handle_response(message) -> str:
    if not isinstance(message, str):
        return f"Invalid input. Please provide a valid string. Received: {type(message)}"
    p_message = message.lower()
    if p_message == "hello":
        return "Hey there!"
    if p_message == "bye":
        return "Goodbye!"
    if p_message == "roll":
        return str(random.randint(1, 6))
    if p_message == "help":
        return "Help is on the way!"
    if p_message[0] == "!":
        base_url = "https://api.mangadex.org"
        title = message[1:]
        r = requests.get(
            f"{base_url}/manga",
            params={"title": title}
        )

        data = r.json()
        # Save the data to a JSON file
        manga_data = data["data"][0]["attributes"]

        name = manga_data["title"]["en"]
        last_chapter = manga_data["lastChapter"]
        return_statement = f"Name: {name}\nLast Chapter: {last_chapter}"
        return return_statement
     
    return "I don't understand you."
