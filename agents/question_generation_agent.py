class QuestionGenerationAgent:
    def generate(self, product):
        questions = {
            "Informational": [
                f"What is {product['name']}?",
                f"What is the concentration of Vitamin C in this product?"
            ],
            "Usage": [
                "How should I apply this serum?",
                "When should I use this serum?"
            ],
            "Safety": [
                "Does this serum have any side effects?",
                "Is mild tingling normal?"
            ],
            "Purchase": [
                "What is the price of this product?",
                "Is this product worth buying?"
            ],
            "Suitability": [
                "Is this serum suitable for oily skin?",
                "Can combination skin use this serum?"
            ]
        }
        return questions
