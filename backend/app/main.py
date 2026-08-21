from fastapi import FastAPI, HTTPException, status

from app.data import RECIPES
from app.models import (
    FavoriteUpdate,
    RecipeCreate,
    RecipeDetail,
    RecipeSummary,
)


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
    favorite: bool | None = None,
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

    if favorite is not None:
        recipes = [
            recipe
            for recipe in recipes
            if recipe["is_favorite"] == favorite
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


def generate_recipe_id() -> str:
    recipe_numbers = [
        int(recipe["id"].split("-")[1])
        for recipe in RECIPES
        if recipe["id"].startswith("recipe-")
    ]

    next_number = max(recipe_numbers, default=0) + 1

    return f"recipe-{next_number:03d}"


@app.post(
    "/api/recipes",
    response_model=RecipeDetail,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(recipe_create: RecipeCreate) -> dict:
    recipe = {
        "id": generate_recipe_id(),
        "title": recipe_create.title,
        "category": recipe_create.category,
        "servings": recipe_create.servings,
        "is_favorite": False,
        "ingredients": [
            ingredient.model_dump()
            for ingredient in recipe_create.ingredients
        ],
        "preparation_tasks": recipe_create.preparation_tasks,
        "steps": [
            {
                "instruction": step.instruction
            }
            for step in recipe_create.steps
        ],
    }

    RECIPES.append(recipe)

    return recipe


@app.put(
    "/api/recipes/{recipe_id}",
    response_model=RecipeDetail,
)
def update_recipe(
    recipe_id: str,
    recipe_update: RecipeCreate,
) -> dict:
    for recipe in RECIPES:
        if recipe["id"] == recipe_id:
            recipe["title"] = recipe_update.title
            recipe["category"] = recipe_update.category
            recipe["servings"] = recipe_update.servings

            recipe["ingredients"] = [
                ingredient.model_dump()
                for ingredient in recipe_update.ingredients
            ]

            recipe["preparation_tasks"] = (
                recipe_update.preparation_tasks
            )

            recipe["steps"] = [
                step.model_dump()
                for step in recipe_update.steps
            ]

            return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Recipe not found",
    )