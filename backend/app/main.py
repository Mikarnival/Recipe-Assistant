from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
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
    db: Session = Depends(get_db),
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

    recipes = crud.get_all_recipes(
        db=db,
        q=q,
        category=category,
        favorite=favorite,
        sort=sort,
    )

    return [
        crud.recipe_to_dict(recipe)
        for recipe in recipes
    ]


@app.get(
    "/api/recipes/{recipe_id}",
    response_model=RecipeDetail,
)
def get_recipe(
    recipe_id: str,
    db: Session = Depends(get_db),
) -> dict:
    recipe = crud.get_recipe(
        db,
        recipe_id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return crud.recipe_to_dict(recipe)


@app.put(
    "/api/recipes/{recipe_id}/favorite",
    response_model=RecipeSummary,
)
def update_recipe_favorite(
    recipe_id: str,
    favorite_update: FavoriteUpdate,
    db: Session = Depends(get_db),
) -> dict:
    recipe = crud.get_recipe(
        db,
        recipe_id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    updated_recipe = crud.update_recipe_favorite(
        db,
        recipe,
        favorite_update.is_favorite,
    )

    return crud.recipe_to_dict(updated_recipe)


@app.post(
    "/api/recipes",
    response_model=RecipeDetail,
    status_code=status.HTTP_201_CREATED,
)
def create_recipe(
    recipe_create: RecipeCreate,
    db: Session = Depends(get_db),
) -> dict:
    recipe = crud.create_recipe(
        db,
        recipe_create,
    )

    return crud.recipe_to_dict(recipe)


@app.put(
    "/api/recipes/{recipe_id}",
    response_model=RecipeDetail,
)
def update_recipe(
    recipe_id: str,
    recipe_update: RecipeCreate,
    db: Session = Depends(get_db),
) -> dict:
    recipe = crud.get_recipe(
        db,
        recipe_id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    updated_recipe = crud.update_recipe(
        db,
        recipe,
        recipe_update,
    )

    return crud.recipe_to_dict(updated_recipe)


@app.delete(
    "/api/recipes/{recipe_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_recipe(
    recipe_id: str,
    db: Session = Depends(get_db),
) -> None:
    recipe = crud.get_recipe(
        db,
        recipe_id,
    )

    if recipe is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    crud.delete_recipe(
        db,
        recipe,
    )