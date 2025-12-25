import json

from product_data import PRODUCT_DATA
from agents.data_parser_agent import DataParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.fictional_product_agent import FictionalProductAgent
from templates.faq_template import FAQTemplate
from templates.product_template import ProductPageTemplate
from templates.comparison_template import ComparisonTemplate


class Orchestrator:
    def run(self):
        # Parse real product
        parser = DataParserAgent()
        product_a = parser.parse(PRODUCT_DATA)

        # Generate questions
        question_agent = QuestionGenerationAgent()
        questions = question_agent.generate(product_a)

        # Generate fictional product
        fictional_agent = FictionalProductAgent()
        product_b = fictional_agent.generate()

        # Generate pages
        faq_page = FAQTemplate().render(questions, product_a)
        product_page = ProductPageTemplate().render(product_a)
        comparison_page = ComparisonTemplate().render(product_a, product_b)

        # Save outputs
        with open("outputs/faq.json", "w") as f:
            json.dump(faq_page, f, indent=4)

        with open("outputs/product_page.json", "w") as f:
            json.dump(product_page, f, indent=4)

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(comparison_page, f, indent=4)

        print("✅ All pages generated successfully!")


if __name__ == "__main__":
    Orchestrator().run()
