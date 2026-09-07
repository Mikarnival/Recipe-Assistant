from sqlalchemy import select
from sqlalchemy.orm import Session

from app import db_models
from app.models import RecipeCreate


def recipe_to_dict(recipe: db_models.Recipe) -> dict:
    return {
        "id": recipe.id,
        "title": recipe.title,
        "category": recipe.category,
        "servings": recipe.servings,
        "is_favorite": recipe.is_favorite,
        "ingredients": [
            {
                "name": ingredient.name,
                "quantity": ingredient.quantity,
                "unit": ingredient.unit,
            }
            for ingredient in recipe.ingredients
        ],
        "preparation_tasks": [
            task.instruction
            for task in recipe.preparation_tasks
        ],
        "steps": [
            {
                "instruction": step.instruction,
            }
            for step in recipe.steps
        ],
    }


def get_recipe(
    db: Session,
    recipe_id: str,
) -> db_models.Recipe | None:
    return db.get(
        db_models.Recipe,
        recipe_id,
    )


def get_all_recipes(
    db: Session,
    q: str | None = None,
    category: str | None = None,
    favorite: bool | None = None,
    sort: str | None = None,
) -> list[db_models.Recipe]:
    statement = select(db_models.Recipe)

    if q is not None and q.strip():
        search_term = f"%{q.strip()}%"

        statement = statement.where(
            db_models.Recipe.title.ilike(search_term)
        )

    if category is not None and category.strip():
        statement = statement.where(
            db_models.Recipe.category.ilike(
            category.strip()
            )
        )

    if favorite is not None:
        statement = statement.where(
            db_models.Recipe.is_favorite
            == favorite
        )

    if sort == "title_asc":
        statement = statement.order_by(
            db_models.Recipe.title.asc()
        )

    elif sort == "title_desc":
        statement = statement.order_by(
            db_models.Recipe.title.desc()
        )

    return list(
        db.scalars(statement).all()
    )


def generate_recipe_id(
    db: Session,
) -> str:
    recipes = get_all_recipes(db)

    recipe_numbers = [
        int(recipe.id.split("-")[1])
        for recipe in recipes
        if recipe.id.startswith("recipe-")
        and recipe.id.split("-")[1].isdigit()
    ]

    next_number = max(
        recipe_numbers,
        default=0,
    ) + 1

    return f"recipe-{next_number:03d}"


def create_recipe(
    db: Session,
    recipe_create: RecipeCreate,
) -> db_models.Recipe:
    recipe = db_models.Recipe(
        id=generate_recipe_id(db),
        title=recipe_create.title,
        category=recipe_create.category,
        servings=recipe_create.servings,
        is_favorite=False,
    )

    recipe.ingredients = [
        db_models.Ingredient(
            position=index,
            name=ingredient.name,
            quantity=ingredient.quantity,
            unit=ingredient.unit,
        )
        for index, ingredient
        in enumerate(recipe_create.ingredients)
    ]

    recipe.preparation_tasks = [
        db_models.PreparationTask(
            position=index,
            instruction=instruction,
        )
        for index, instruction
        in enumerate(recipe_create.preparation_tasks)
    ]

    recipe.steps = [
        db_models.CookingStep(
            position=index,
            instruction=step.instruction,
        )
        for index, step
        in enumerate(recipe_create.steps)
    ]

    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe


def update_recipe(
    db: Session,
    recipe: db_models.Recipe,
    recipe_update: RecipeCreate,
) -> db_models.Recipe:
    recipe.title = recipe_update.title
    recipe.category = recipe_update.category
    recipe.servings = recipe_update.servings

    recipe.ingredients.clear()

    recipe.ingredients.extend(
        [
            db_models.Ingredient(
                position=index,
                name=ingredient.name,
                quantity=ingredient.quantity,
                unit=ingredient.unit,
            )
            for index, ingredient
            in enumerate(recipe_update.ingredients)
        ]
    )

    recipe.preparation_tasks.clear()

    recipe.preparation_tasks.extend(
        [
            db_models.PreparationTask(
                position=index,
                instruction=instruction,
            )
            for index, instruction
            in enumerate(recipe_update.preparation_tasks)
        ]
    )

    recipe.steps.clear()

    recipe.steps.extend(
        [
            db_models.CookingStep(
                position=index,
                instruction=step.instruction,
            )
            for index, step
            in enumerate(recipe_update.steps)
        ]
    )

    db.commit()
    db.refresh(recipe)

    return recipe


def delete_recipe(
    db: Session,
    recipe: db_models.Recipe,
) -> None:
    db.delete(recipe)
    db.commit()

def update_recipe_favorite(
    db: Session,
    recipe: db_models.Recipe,
    is_favorite: bool,
) -> db_models.Recipe:
    recipe.is_favorite = is_favorite

    db.commit()
    db.refresh(recipe)

    return recipe