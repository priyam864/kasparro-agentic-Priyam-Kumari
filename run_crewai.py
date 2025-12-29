import json
from dotenv import load_dotenv

load_dotenv()

from crewai_system.crew import run_faq_crew


def main():
    result = run_faq_crew()

    # ✅ Extract raw JSON output from CrewOutput
    output = result.raw if hasattr(result, "raw") else result

    with open("outputs/faq.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print("✅ FAQ JSON generated successfully with CrewAI!")


if __name__ == "__main__":
    main()
