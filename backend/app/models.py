from pydantic import BaseModel


class RecipeSummary(BaseModel):
    id: str
    title: str
    category: str
    servings: int


class Ingredient(BaseModel):
    name: str
    quantity: float
    unit: str


class CookingStep(BaseModel):
    instruction: str


class RecipeDetail(BaseModel):
    id: str
    title: str
    category: str
    servings: int
    ingredients: list[Ingredient]
    preparation_tasks: list[str]
    steps: list[CookingStep]