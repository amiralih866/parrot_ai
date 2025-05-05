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
            return f"داری از خط قرمز ها عدول میکنی حواسم بهت هست: {error_message}"
        elif "rate" in error_message.lower() and "limit" in error_message.lower():
            return f"حاجی من ذهنم انقدر رو جواب نمیده: {error_message}. بعدا تلاش کن شاید فهمیدم."
        elif "invalid" in error_message.lower() or "api key" in error_message.lower():
            return f"خودت فهمیدی چی گفتی؟: {error_message}"
        else:
            return f"اینو انیشتن هم نمیفهمه چه برسه به من: {error_message}"
