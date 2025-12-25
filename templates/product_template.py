class ProductPageTemplate:
    def render(self, product):
        return {
            "name": product["name"],
            "concentration": product["concentration"],
            "skin_type": product["skin_type"],
            "key_ingredients": product["ingredients"],
            "benefits": product["benefits"],
            "usage": product["usage"],
            "side_effects": product["side_effects"],
            "price": product["price"]
        }
