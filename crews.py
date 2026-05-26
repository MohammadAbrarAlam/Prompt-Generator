import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # type: ignore

model = genai.GenerativeModel("gemini-2.5-flash")  # type: ignore


def run_prompt_generator(description, style):
    prompt = f"""
    Generate a detailed AI prompt for:

    Description: {description}
    Style: {style}

    Return only the final prompt.
    """

    response = model.generate_content(prompt)
    return response.text