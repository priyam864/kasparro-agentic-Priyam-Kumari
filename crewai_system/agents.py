import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import ChatOpenAI

# 🔑 LOAD ENV HERE (CRITICAL)
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)


product_analyst_agent = Agent(
    role="Product Analyst",
    goal="Understand and extract structured insights from the provided product data",
    backstory=(
        "You are an expert product analyst who specializes in understanding skincare "
        "products strictly from provided input data without adding external facts."
    ),
    llm=llm,
    verbose=True
)


faq_generator_agent = Agent(
    role="FAQ Generator",
    goal="Generate comprehensive user FAQs strictly based on product data",
    backstory=(
        "You are an AI assistant responsible for generating clear, helpful, and "
        "accurate user FAQs based only on the provided product information. "
        "You must generate at least 15 FAQs."
    ),
    llm=llm,
    verbose=True
)


content_structuring_agent = Agent(
    role="Content Structuring Agent",
    goal="Convert generated content into strict, schema-compliant JSON outputs",
    backstory=(
        "You specialize in transforming unstructured AI-generated text into "
        "validated, machine-readable JSON formats while strictly following schemas."
    ),
    llm=llm,
    verbose=True
)
