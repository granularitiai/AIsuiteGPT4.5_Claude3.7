# -*- coding: utf-8 -*-

!pip install aisuite[all]

import os
from getpass import getpass

import aisuite as ai

os.environ['OPENAI_API_KEY'] = getpass('Enter your OPENAI API key: ')
os.environ['ANTHROPIC_API_KEY'] = getpass('Enter your ANTHROPIC API key: ')

from pprint import pprint as pp
# Set a custom width for pretty-printing
def pprint(data, width=80):
    """Pretty print data with a specified width."""
    pp(data, width=width)# List of model identifiers to query

def ask(message, sys_message="You are a helpful agent.",
         model="groq:llama-3.2-3b-preview"):
    # Initialize the AI client for accessing the language model
    client = ai.Client()

    # Construct the messages list for the chat
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": message}
    ]

    # Send the messages to the model and get the response
    response = client.chat.completions.create(model=model, messages=messages)

    # Return the content of the model's response
    return response.choices[0].message.content

    #groq:llama-3.2-3b-preview

providers = [
    'openai:gpt-4.5-preview-2025-02-27',
    'openai:gpt-4o-2024-08-06'
]

# Initialize a list to hold the responses from each provider
responses = []

# Loop through each provider and get a response for the specified question
question = "How would you console a friend who just lost their job, ensuring your response is empathetic and supportive?"

for provider in providers:
    response = ask(question, model=provider)
    responses.append((provider, response))

# Print the formatted output
print("\n=== AI Model Responses ===\n")
for provider, response in responses:
    print(f"🔹 **{provider}**\n")
    print(response)
    print("\n" + "-" * 80 + "\n")

