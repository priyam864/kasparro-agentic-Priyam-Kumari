from pydantic import BaseModel, Field
from typing import List


class FAQItem(BaseModel):
    question: str = Field(..., description="User question")
    answer: str = Field(..., description="Answer strictly based on product data")


class FAQPage(BaseModel):
    product_name: str
    faqs: List[FAQItem] = Field(..., min_items=15)
