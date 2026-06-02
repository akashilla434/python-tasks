# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():

    client = genai.Client(
       api_key="AQ.Ab8RN6KGuq_3bd20M00trPOR45nnXLxAM0_iCSocvi-gkrbgbQ"

    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="What is Python?"
    )

    print(response.text)

if __name__ == "__main__":
    generate()
