import openai
import os
from modules.sense import speak
def chatgpt(prompt):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = prompt.lower()

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    speak(response)
    print(response)