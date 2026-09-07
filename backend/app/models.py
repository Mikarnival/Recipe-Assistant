from typing import Annotated

from pydantic import BaseModel, Field


NonEmptyString = Annotated[
    str,
    Field(min_length=1),
]


class RecipeSummary(BaseModel):
    id: str
    title: str
    category: str
    servings: int
    is_favorite: bool


class FavoriteUpdate(BaseModel):
    is_favorite: bool


class Ingredient(BaseModel):
    name: NonEmptyString
    quantity: float = Field(gt=0)
    unit: NonEmptyString


class CookingStep(BaseModel):
    instruction: NonEmptyString


class RecipeCreate(BaseModel):
    title: NonEmptyString
    category: NonEmptyString
    servings: int = Field(gt=0)
    ingredients: list[Ingredient] = Field(min_length=1)
    preparation_tasks: list[str] = Field(default_factory=list)
    steps: list[CookingStep] = Field(min_length=1)


class RecipeDetail(BaseModel):
    id: str
    title: NonEmptyString
    category: NonEmptyString
    servings: int = Field(gt=0)
    is_favorite: bool
    ingredients: list[Ingredient]
    preparation_tasks: list[str]
    steps: list[CookingStep]

class RecipeImport(RecipeCreate):
    id: NonEmptyString
    is_favorite: bool = False