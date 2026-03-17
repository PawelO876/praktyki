import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def send_message(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": messages,
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()