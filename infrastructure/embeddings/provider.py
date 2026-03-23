import os


def embed_text(text: str):
    use_openai = os.getenv("USE_OPENAI", "false").lower() == "true"
    api_key = os.getenv("OPENAI_API_KEY")

    # --- DEV MODE (no API key required) ---
    if not use_openai or not api_key:
        return [0.0] * 1536

    # --- PROD MODE ---
    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(model="text-embedding-3-small", input=text)

    return response.data[0].embedding
