from product_data import PRODUCT_DATA
from agents.data_parser_agent import DataParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from templates.faq_template import FAQTemplate

parser = DataParserAgent()
product = parser.parse(PRODUCT_DATA)

question_agent = QuestionGenerationAgent()
questions = question_agent.generate(product)

faq_template = FAQTemplate()
faq_page = faq_template.render(questions, product)

print(faq_page)
