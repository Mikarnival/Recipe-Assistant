from pydantic import BaseModel

class RecipeSummary(BaseModel):
    id: str
    title: str
    category: str
    servings: int