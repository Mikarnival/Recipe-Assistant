import json
from pathlib import Path

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import db_models
from app.database import engine
from app.models import RecipeImport


BASE_DIR = Path(__file__).resolve().parent.parent
SEED_DATA_DIR = BASE_DIR / "seed_data"


def load_recipe_file(file_path: Path) -> RecipeImport:
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    return RecipeImport.model_validate(data)


def create_recipe_from_import(
    db: Session,
    recipe_data: RecipeImport,
) -> db_models.Recipe:
    recipe = db_models.Recipe(
        id=recipe_data.id,
        title=recipe_data.title,
        category=recipe_data.category,
        servings=recipe_data.servings,
        is_favorite=recipe_data.is_favorite,
    )

    recipe.ingredients = [
        db_models.Ingredient(
            position=index,
            name=ingredient.name,
            quantity=ingredient.quantity,
            unit=ingredient.unit,
        )
        for index, ingredient
        in enumerate(recipe_data.ingredients)
    ]

    recipe.preparation_tasks = [
        db_models.PreparationTask(
            position=index,
            instruction=instruction,
        )
        for index, instruction
        in enumerate(recipe_data.preparation_tasks)
    ]

    recipe.steps = [
        db_models.CookingStep(
            position=index,
            instruction=step.instruction,
        )
        for index, step
        in enumerate(recipe_data.steps)
    ]

    return recipe


def import_recipes() -> None:
    json_files = sorted(
        SEED_DATA_DIR.glob("*.json")
    )

    if not json_files:
        print(
            f"No JSON files found in "
            f"{SEED_DATA_DIR}"
        )
        return

    added_count = 0
    skipped_count = 0
    failed_count = 0

    with Session(engine) as db:
        for file_path in json_files:
            try:
                recipe_data = load_recipe_file(
                    file_path
                )

                existing_recipe = db.get(
                    db_models.Recipe,
                    recipe_data.id,
                )

                if existing_recipe is not None:
                    print(
                        f"SKIP: {file_path.name} "
                        f"({recipe_data.id} already exists)"
                    )

                    skipped_count += 1
                    continue

                recipe = create_recipe_from_import(
                    db,
                    recipe_data,
                )

                db.add(recipe)

                print(
                    f"ADD: {file_path.name} "
                    f"({recipe_data.id})"
                )

                added_count += 1

            except json.JSONDecodeError as error:
                print(
                    f"ERROR: {file_path.name} "
                    f"contains invalid JSON: {error}"
                )

                failed_count += 1

            except ValidationError as error:
                print(
                    f"ERROR: {file_path.name} "
                    f"failed recipe validation:"
                )

                print(error)

                failed_count += 1

        if failed_count > 0:
            db.rollback()

            print()
            print(
                "Import cancelled because "
                "one or more files are invalid."
            )

            return

        db.commit()

    print()
    print("Import complete.")
    print(f"Added:   {added_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Failed:  {failed_count}")


if __name__ == "__main__":
    import_recipes()