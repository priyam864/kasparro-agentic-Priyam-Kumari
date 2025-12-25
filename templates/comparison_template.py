class ComparisonTemplate:
    def render(self, product_a, product_b):
        return {
            "product_a": product_a["name"],
            "product_b": product_b["name"],
            "comparison": {
                "ingredients": {
                    product_a["name"]: product_a["ingredients"],
                    product_b["name"]: product_b["ingredients"]
                },
                "benefits": {
                    product_a["name"]: product_a["benefits"],
                    product_b["name"]: product_b["benefits"]
                },
                "price": {
                    product_a["name"]: product_a["price"],
                    product_b["name"]: product_b["price"]
                }
            }
        }
