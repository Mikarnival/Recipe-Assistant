from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_recipes_returns_200() -> None:
    response = client.get("/api/recipes")

    assert response.status_code == 200


def test_get_recipes_returns_all_recipes() -> None:
    response = client.get("/api/recipes")

    data = response.json()

    assert len(data) == 2


def test_get_recipes_returns_expected_field_types() -> None:
    response = client.get("/api/recipes")

    data = response.json()

    for recipe in data:
        assert isinstance(recipe["id"], str)
        assert isinstance(recipe["title"], str)
        assert isinstance(recipe["category"], str)
        assert isinstance(recipe["servings"], int)


def test_get_recipes_returns_empty_list_when_no_recipes(monkeypatch) -> None:
    from app import main

    monkeypatch.setattr(main, "RECIPES", [])

    response = client.get("/api/recipes")

    assert response.status_code == 200
    assert response.json() == []


def test_get_recipe_by_id_returns_200() -> None:
    response = client.get("/api/recipes/recipe-001")

    assert response.status_code == 200


def test_get_recipe_by_id_returns_expected_recipe() -> None:
    response = client.get("/api/recipes/recipe-001")

    data = response.json()

    assert data["id"] == "recipe-001"
    assert data["title"] == "Tomato and Egg Stir-Fry"


def test_get_recipe_by_id_returns_expected_fields() -> None:
    response = client.get("/api/recipes/recipe-001")

    data = response.json()

    expected_fields = {
        "id",
        "title",
        "category",
        "servings",
        "ingredients",
        "preparation_tasks",
        "steps",
    }

    assert set(data.keys()) == expected_fields


def test_get_recipe_by_id_returns_404_for_unknown_recipe() -> None:
    response = client.get("/api/recipes/unknown-recipe")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Recipe not found"
    }


def test_search_recipes_by_full_title() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": "Beef Noodle Soup"},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"
    assert data[0]["title"] == "Beef Noodle Soup"


def test_search_recipes_by_partial_title() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": "Noodle"},
    )

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_search_recipes_is_case_insensitive() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": "beef noodle soup"},
    )

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_search_recipes_returns_empty_list_for_no_match() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": "Pizza"},
    )

    assert response.status_code == 200
    assert response.json() == []


def test_search_recipes_with_empty_query_returns_all_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": ""},
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2


def test_search_recipes_with_whitespace_query_returns_all_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={"q": "   "},
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2