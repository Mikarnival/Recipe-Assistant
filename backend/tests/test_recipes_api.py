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