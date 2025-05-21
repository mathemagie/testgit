# Import required libraries
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the ANTHROPIC_API_KEY from environment variables
api_key = os.getenv('ANTHROPIC_API_KEY')

# Check if the API key exists
if api_key:
    print("API key loaded successfully!")
    # For security, we only print the first few characters
    print(f"API key starts with: {api_key[:4]}...")
else:
    print("Warning: ANTHROPIC_API_KEY not found in environment variables")


dqskdjqskdjqskdjsqkh