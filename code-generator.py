"""
sample code generator using OpenAI
"""
import os
from dotenv import load_dotenv
from openai import OpenAI
openai.api_key = 'YOUR_API_KEY'

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv('OPENAI_API_KEY')
)

response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "def add(a, b):\n    "}
            ],
            model="gpt-4o-mini"
        )
print(response.choices[0].message.content)
