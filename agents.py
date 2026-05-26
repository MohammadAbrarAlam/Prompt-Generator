from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()


llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)


image_prompt_agent = Agent(
    role="AI Prompt Generator",

    goal="""
    Generate creative, professional prompts
    from uploaded images, posters and videos
    based on user-selected style.
    """,

    backstory="""
    You are an expert AI prompt engineer.
    You understand photography, lighting,
    mood, emotions, realism and cinematic composition.
    """,

    llm=llm,
    verbose=True
)