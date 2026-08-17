from fastapi import FastAPI, HTTPException, status

from app.data import RECIPES
from app.models import FavoriteUpdate, RecipeDetail, RecipeSummary


app = FastAPI(
    title="Recipe Assistant API",
)


@app.get(
    "/api/recipes",
    response_model=list[RecipeSummary],
)
def get_recipes(
    q: str | None = None,
    category: str | None = None,
    sort: str | None = None,
) -> list[dict]:
    valid_sort_values = {
        "title_asc",
        "title_desc",
    }

    if sort is not None and sort.strip():
        if sort not in valid_sort_values:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported sort value",
            )

    recipes = list(RECIPES)

    if q is not None and q.strip():
        search_term = q.strip().lower()

        recipes = [
            recipe
            for recipe in recipes
            if search_term in recipe["title"].lower()
        ]

    if category is not None and category.strip():
        category_term = category.strip().lower()

        recipes = [
            recipe
            for recipe in recipes
            if recipe["category"].lower() == category_term
        ]

    if sort == "title_asc":
        recipes.sort(
            key=lambda recipe: recipe["title"].lower()
        )

    elif sort == "title_desc":
        recipes.sort(
            key=lambda recipe: recipe["title"].lower(),
            reverse=True,
        )

    return recipes


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


@app.put(
    "/api/recipes/{recipe_id}/favorite",
    response_model=RecipeSummary,
)
def update_recipe_favorite(
    recipe_id: str,
    favorite_update: FavoriteUpdate,
) -> dict:
    for recipe in RECIPES:
        if recipe["id"] == recipe_id:
            recipe["is_favorite"] = favorite_update.is_favorite
            return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Recipe not found",
    )

