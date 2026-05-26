from crewai import Crew
from tasks import generate_prompt_task


def run_prompt_generator(description, style):
    task = generate_prompt_task(description, style)

    crew = Crew(
        agents=[agent for agent in [task.agent] if agent is not None],
        tasks=[task]
    )

    result = crew.kickoff()
    return result