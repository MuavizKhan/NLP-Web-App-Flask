import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the modern unified client architecture
# It automatically picks up GEMINI_API_KEY from your .env file
client = genai.Client()


def analyze_text(text, analysis_type):
    """
    Unified execution pipeline using the modern google-genai SDK.
    """
    formatting_instruction = "\n\nIMPORTANT: Do not use raw markdown tags like **, ##, or *. Present titles neatly on their own line, followed by clean list details below them."

    prompts = {
        "sentiment": "Analyze the sentiment of the following text. Return a clear breakdown of positive, negative, or neutral leaning with percentage weights." + formatting_instruction,
        "emotion": "Perform detailed emotion prediction. Provide percentage distributions across Joy, Sadness, Anger, Fear, and Surprise." + formatting_instruction,
        "ner": "Extract all major Named Entities (NER) from this text. List them clearly under distinct category headers such as Persons, Organizations, and Locations." + formatting_instruction,
        "summarizer": "Provide a high-impact summary. Include a target read-time estimate, a single-sentence TL;DR, and core takeaways." + formatting_instruction,
        "copilot": "Act as an interactive AI Copilot. Analyze the text, critique its structure, and give actionable suggestions to improve it." + formatting_instruction,
        "grammar": "Act as a professional copyeditor. Rewrite the text to eliminate grammatical issues and optimize it into a polished, executive corporate tone." + formatting_instruction,
        "abuse": "Perform safety and abuse detection. Flag any toxicity, profanity, hate speech, or aggressive intent, providing a clear risk severity ranking (Low/Medium/High)." + formatting_instruction
    }

    system_prompt = prompts.get(analysis_type, "Analyze the text thoroughly.")
    full_prompt = f"{system_prompt}\n\nText to analyze:\n\"\"\"{text}\"\"\""

    try:
        # Modern SDK generation method call
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Engine Analysis Error: {str(e)}"