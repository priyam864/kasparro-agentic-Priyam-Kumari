class FAQTemplate:
    def render(self, questions, product):
        faqs = []

        for category in questions:
            for question in questions[category]:
                faqs.append({
                    "question": question,
                    "answer": product["usage"]
                })

        return {
            "product": product["name"],
            "faqs": faqs[:5]
        }
