from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.db_models import (
    CookingStep,
    Ingredient,
    PreparationTask,
    Recipe,
)
from app.main import app


TEST_DATABASE_URL = "sqlite://"


test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)


TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    expire_on_commit=False,
)


def seed_test_recipes(
    db: Session,
) -> None:
    tomato_egg = Recipe(
        id="recipe-001",
        title="Tomato and Egg Stir-Fry",
        category="Chinese",
        servings=2,
        is_favorite=False,
    )

    tomato_egg.ingredients = [
        Ingredient(
            position=0,
            name="Egg",
            quantity=3,
            unit="piece",
        ),
        Ingredient(
            position=1,
            name="Tomato",
            quantity=2,
            unit="piece",
        ),
        Ingredient(
            position=2,
            name="Cooking oil",
            quantity=15,
            unit="ml",
        ),
        Ingredient(
            position=3,
            name="Salt",
            quantity=2,
            unit="g",
        ),
    ]

    tomato_egg.preparation_tasks = [
        PreparationTask(
            position=0,
            instruction="Beat the eggs.",
        ),
        PreparationTask(
            position=1,
            instruction="Cut the tomatoes into chunks.",
        ),
    ]

    tomato_egg.steps = [
        CookingStep(
            position=0,
            instruction="Heat the cooking oil in a pan.",
        ),
        CookingStep(
            position=1,
            instruction=(
                "Add the eggs and stir-fry "
                "until softly set."
            ),
        ),
        CookingStep(
            position=2,
            instruction="Remove the eggs from the pan.",
        ),
        CookingStep(
            position=3,
            instruction=(
                "Add the tomatoes and cook until softened."
            ),
        ),
        CookingStep(
            position=4,
            instruction=(
                "Return the eggs to the pan, "
                "season with salt, and mix well."
            ),
        ),
    ]

    beef_noodle = Recipe(
        id="recipe-002",
        title="Beef Noodle Soup",
        category="Noodles",
        servings=2,
        is_favorite=False,
    )

    beef_noodle.ingredients = [
        Ingredient(
            position=0,
            name="Beef",
            quantity=300,
            unit="g",
        ),
        Ingredient(
            position=1,
            name="Noodles",
            quantity=200,
            unit="g",
        ),
        Ingredient(
            position=2,
            name="Water",
            quantity=1000,
            unit="ml",
        ),
        Ingredient(
            position=3,
            name="Light soy sauce",
            quantity=20,
            unit="ml",
        ),
    ]

    beef_noodle.preparation_tasks = [
        PreparationTask(
            position=0,
            instruction="Cut the beef into pieces.",
        ),
    ]

    beef_noodle.steps = [
        CookingStep(
            position=0,
            instruction="Add the beef and water to a pot.",
        ),
        CookingStep(
            position=1,
            instruction="Bring to a boil and remove any foam.",
        ),
        CookingStep(
            position=2,
            instruction="Simmer the beef until tender.",
        ),
        CookingStep(
            position=3,
            instruction=(
                "Season the broth with light soy sauce."
            ),
        ),
        CookingStep(
            position=4,
            instruction="Cook the noodles separately.",
        ),
        CookingStep(
            position=5,
            instruction=(
                "Place the noodles in bowls and "
                "pour the beef broth over them."
            ),
        ),
    ]

    db.add_all(
        [
            tomato_egg,
            beef_noodle,
        ]
    )

    db.commit()


@pytest.fixture(autouse=True)
def reset_database() -> Generator[None, None, None]:
    Base.metadata.drop_all(
        bind=test_engine
    )

    Base.metadata.create_all(
        bind=test_engine
    )

    with TestingSessionLocal() as db:
        seed_test_recipes(db)

    yield


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[
        Session,
        None,
        None,
    ]:
        db = TestingSessionLocal()

        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = (
        override_get_db
    )

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def db() -> Generator[Session, None, None]:
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()