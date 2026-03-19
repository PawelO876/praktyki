
import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

# ──────────────────────────────────────────────
# Funkcja do komunikacji z OpenRouter.ai
# ──────────────────────────────────────────────
def chat_with_openrouter(prompt: str, model: str = "", api_key: str | None = None) -> str:
    """
    Wysyła zapytanie do OpenRouter.ai i zwraca odpowiedź modelu.
    """
    api_key = api_key or os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        raise ValueError(
            "Brak klucza API! Ustaw zmienną OPENROUTER_API_KEY "
            "lub przekaż api_key jako argument."
        )

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://example.com",
        "X-Title": "OpenRouter Demo",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Jesteś pomocnym asystentem. Odpowiadaj zwięźle."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 512,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    if response.status_code != 200:
        raise RuntimeError(f"Błąd API ({response.status_code}): {response.text}")

    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Nieoczekiwany format odpowiedzi: {json.dumps(data, indent=2)}")

# ──────────────────────────────────────────────
# Import payloadów
# ──────────────────────────────────────────────
from payloads import payload_1, payload_2, payload_3, payload_4, payload_5

payload_list = [payload_1, payload_2, payload_3, payload_4, payload_5]

# ──────────────────────────────────────────────
# Główna pętla – wysyłanie wszystkich payloadów
# ──────────────────────────────────────────────
if __name__ == "__main__":

    API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    MODEL = "openrouter/free"

    print("=" * 60)
    print("🚀 OpenRouter Demo – wysyłanie 5 payloadów")
    print("=" * 60)

    for i, payload in enumerate(payload_list, 1):
        try:
            answer = chat_with_openrouter(
                prompt=payload["messages"][1]["content"],
                model=payload["model"],
                api_key=API_KEY
            )
            print(f"\n✅ Odpowiedź dla payload_{i}:")
            print(answer)
        except Exception as e:
            print(f"\n❌ Błąd przy payload_{i}: {e}")

    print("\n" + "=" * 60)