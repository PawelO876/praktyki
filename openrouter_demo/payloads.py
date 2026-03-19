# payloads.py

payload_1 = {
    "model": "openrouter/free",
    "messages": [
        {"role": "system", "content": "Jesteś eksperckim kalkulatorem naukowym."},
        {"role": "user", "content": "Oblicz (5^3 + log10(100)) / sin(30°)"}
    ],
    "temperature": 0.1,
    "max_tokens": 200
}

payload_2 = {
    "model": "openrouter/free",
    "messages": [
        {"role": "system", "content": "Jesteś cierpliwym nauczycielem angielskiego."},
        {"role": "user", "content": "Wytłumacz różnicę między 'present perfect' a 'past simple'."}
    ],
    "temperature": 0.6,
    "max_tokens": 300
}

payload_3 = {
    "model": "openrouter/free",
    "messages": [
        {"role": "system", "content": "Jesteś kreatywnym copywriterem marketingowym."},
        {"role": "user", "content": "Stwórz trzy chwytliwe slogany dla aplikacji fitness."}
    ],
    "temperature": 1.2,
    "max_tokens": 250
}

payload_4 = {
    "model": "openrouter/free",
    "messages": [
        {"role": "system", "content": "Jesteś empatycznym psychologiem online."},
        {"role": "user", "content": "Czuję się zestresowany pracą. Co mogę zrobić?"}
    ],
    "temperature": 0.8,
    "max_tokens": 500
}

payload_5 = {
    "model": "openrouter/free",
    "messages": [
        {"role": "system", "content": "Jesteś doświadczonym programistą i debuggerem."},
        {"role": "user", "content": "Mój kod rzuca 'IndexError: list index out of range'. Pomóż."}
    ],
    "temperature": 0.2,
    "max_tokens": 400
}