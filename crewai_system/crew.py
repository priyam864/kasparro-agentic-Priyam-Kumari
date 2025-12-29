from crewai import Crew
from crewai_system.agents import (
    product_analyst_agent,
    faq_generator_agent,
    content_structuring_agent
)
from crewai_system.tasks import (
    product_analysis_task,
    faq_generation_task,
    content_structuring_task
)


def run_faq_crew():
    crew = Crew(
        agents=[
            product_analyst_agent,
            faq_generator_agent,
            content_structuring_agent
        ],
        tasks=[
            product_analysis_task,
            faq_generation_task,
            content_structuring_task
        ],
        verbose=True
    )

    result = crew.kickoff()
    return result
