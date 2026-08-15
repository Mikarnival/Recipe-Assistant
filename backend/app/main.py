from fastapi import FastAPI, HTTPException, status

from app.data import RECIPES
from app.models import RecipeDetail, RecipeSummary

app = FastAPI(
    title="Recipe Assistant API",
)

@app.get(
    "/api/recipes",
    response_model=list[RecipeSummary],
)
def get_recipes(
    q: str | None = None,
) -> list[dict]:
    if q is None or not q.strip():
        return RECIPES

    search_term = q.strip().lower()

    return [
        recipe
        for recipe in RECIPES
        if search_term in recipe["title"].lower()
    ]


@app.get(
    "/api/recipes/{recipe_id}",
    response_model=RecipeDetail,
)
def get_recipe(recipe_id: str) -> dict:
    for recipe in RECIPES:
        if recipe["id"] == recipe_id:
            return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Recipe not found",
    )