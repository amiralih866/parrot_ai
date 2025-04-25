import tracemalloc
from google import genai as gen
import asyncio

tracemalloc.start()

GEMINI_TOKEN = "AIzaSyCFnBbFO28_c1xI92Jzic871WvSDboKmA8"  # Replace with your actual API key


def ai(ask: str):
    client = gen.Client(api_key=GEMINI_TOKEN)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=ask
    )
    print(response.text)
    return response.text
