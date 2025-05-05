import tracemalloc
from google import genai as gen
import logging

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

tracemalloc.start()

GEMINI_TOKEN = "AIzaSyCFnBbFO28_c1xI92Jzic871WvSDboKmA8"  # Replace with your actual API key


def ai(ask: str):
    try:
        client = gen.Client(api_key=GEMINI_TOKEN)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=ask
        )
        return response.text
    except Exception as e:
        # Properly categorize the error based on the exception string
        error_message = str(e)

        if "blocked" in error_message.lower() or "safety" in error_message.lower():
            return f"Content policy violation: {error_message}"
        elif "rate" in error_message.lower() and "limit" in error_message.lower():
            return f"Rate limit exceeded: {error_message}. Please try again later."
        elif "invalid" in error_message.lower() or "api key" in error_message.lower():
            return f"Invalid input or configuration: {error_message}"
        else:
            return f"An unexpected error occurred: {error_message}"
