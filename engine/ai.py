import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_api_key():
    """
    Looks for the key in two places:
    1. st.secrets - used when deployed on Streamlit Community Cloud
    2. .env file - used for local development
    """

    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY")


def generate_ai_recommendation(prompt):

    try:
        api_key = get_api_key()

        if not api_key:
            return "⚠️ Groq API key is not configured."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are NutriNyx AI, a nutrition explanation assistant. "
                        "Use the nutritional information and recommendations "
                        "provided in the user's prompt. "
                        "Give concise, practical and easy-to-understand advice."
                        "1. A short health summary."
                        "2. Three personalized suggestions."
                        "3. Keep the response below 120 words. "
                        "4. Do not invent nutritional values. "
                        "5. Do not diagnose medical conditions."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            return (
                "⏳ AI service is temporarily rate-limited. "
                "Please try again shortly."
            )

        if "401" in error_message or "authentication" in error_message.lower():
            return (
                "⚠️ AI authentication failed. "
                "Please check the Groq API key."
            )

        return (
            "⚠️ Unable to generate the AI recommendation right now."
        )
