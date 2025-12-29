from crewai import Task
from crewai_system.agents import (
    product_analyst_agent,
    faq_generator_agent,
    content_structuring_agent
)
from crewai_system.schemas import FAQPage


product_analysis_task = Task(
    description=(
        "Analyze the given product data and extract a clear understanding of "
        "the product, including its purpose, ingredients, benefits, usage, "
        "side effects, target skin types, and price. "
        "Use only the provided input data."
    ),
    expected_output=(
        "A structured understanding of the product suitable for downstream "
        "content generation."
    ),
    agent=product_analyst_agent
)


faq_generation_task = Task(
    description=(
        "Using the analyzed product understanding, generate at least 15 distinct, "
        "user-focused FAQs with accurate answers. "
        "Do not add any information beyond the provided product data."
    ),
    expected_output=(
        "A list of at least 15 FAQ question-answer pairs related to the product."
    ),
    agent=faq_generator_agent
)


content_structuring_task = Task(
    description=(
        "Convert the generated FAQ content into a strict JSON format that "
        "complies with the provided FAQPage schema. "
        "Ensure there are at least 15 FAQs and all fields are correctly populated."
    ),
    expected_output="A schema-compliant FAQPage JSON object.",
    output_pydantic=FAQPage,
    agent=content_structuring_agent
)
