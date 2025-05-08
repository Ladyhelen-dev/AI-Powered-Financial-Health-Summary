import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class FinancialAnalyzer:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def analyze(self, text_data):
        """Sends text data to OpenAI and returns a financial summary."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial assistant that analyzes user bank statements and provides summaries."},
                    {"role": "user", "content": f"Analyze this bank statement and give a financial summary:\n{text_data}"}
                ],
                temperature=0.5,
                max_tokens=500
            )
            return response['choices'][0]['message']['content'].strip()

        except openai.error.OpenAIError as e:
            print(f"❌ Error with OpenAI API: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return None
