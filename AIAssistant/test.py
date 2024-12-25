import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Print the API key to verify it's loaded (for testing purposes)
print(f"OpenAI API Key: {openai_api_key}")