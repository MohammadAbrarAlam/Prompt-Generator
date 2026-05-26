from crewai import Task
from agents import image_prompt_agent


def generate_prompt_task(description, style):
    return Task(
        description=f"""
        Analyze this media description:
        {description}

        Generate a {style} AI prompt.
        """,
        agent=image_prompt_agent,
        expected_output="Detailed prompt ready for image generation tools"
    )