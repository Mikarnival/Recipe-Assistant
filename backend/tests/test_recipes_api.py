from fastapi.testclient import TestClient
import pytest

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
        assert isinstance(recipe["is_favorite"], bool)


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
        "is_favorite",
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


def test_get_recipes_returns_favorite_state() -> None:
    response = client.get("/api/recipes")

    data = response.json()

    for recipe in data:
        assert isinstance(recipe["is_favorite"], bool)


def test_mark_recipe_as_favorite() -> None:
    response = client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": True},
    )

    assert response.status_code == 200
    assert response.json()["is_favorite"] is True


def test_remove_recipe_from_favorites() -> None:
    client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": True},
    )

    response = client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": False},
    )

    assert response.status_code == 200
    assert response.json()["is_favorite"] is False


def test_update_favorite_returns_404_for_unknown_recipe() -> None:
    response = client.put(
        "/api/recipes/unknown-recipe/favorite",
        json={"is_favorite": True},
    )

    assert response.status_code == 404


def test_filter_recipes_by_category() -> None:
    response = client.get(
        "/api/recipes",
        params={"category": "Noodles"},
    )

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_filter_recipes_by_category_is_case_insensitive() -> None:
    response = client.get(
        "/api/recipes",
        params={"category": "noodles"},
    )

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_filter_recipes_returns_empty_list_for_no_match() -> None:
    response = client.get(
        "/api/recipes",
        params={"category": "Italian"},
    )

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize(
    ("sort_value", "expected_titles"),
    [
        (
            "title_asc",
            [
                "Beef Noodle Soup",
                "Tomato and Egg Stir-Fry",
            ],
        ),
        (
            "title_desc",
            [
                "Tomato and Egg Stir-Fry",
                "Beef Noodle Soup",
            ],
        ),
    ],
)
def test_sort_recipes_by_title(
    sort_value: str,
    expected_titles: list[str],
) -> None:
    response = client.get(
        "/api/recipes",
        params={"sort": sort_value},
    )

    data = response.json()

    titles = [
        recipe["title"]
        for recipe in data
    ]

    assert titles == expected_titles


def test_search_and_filter_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={
            "q": "Beef",
            "category": "Noodles",
        },
    )

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_search_filter_and_sort_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={
            "q": "Noodle",
            "category": "Noodles",
            "sort": "title_asc",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"


def test_sort_recipes_returns_400_for_unsupported_value() -> None:
    response = client.get(
        "/api/recipes",
        params={"sort": "unknown"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Unsupported sort value"
    }


def test_sort_recipes_with_empty_value_returns_all_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={"sort": ""},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2


def test_sort_recipes_with_whitespace_value_returns_all_recipes() -> None:
    response = client.get(
        "/api/recipes",
        params={"sort": "   "},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2


def test_filter_favorite_recipes() -> None:
    client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": True},
    )
    client.put(
        "/api/recipes/recipe-002/favorite",
        json={"is_favorite": False},
    )

    response = client.get(
        "/api/recipes",
        params={"favorite": True},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-001"
    assert data[0]["is_favorite"] is True


def test_filter_non_favorite_recipes() -> None:
    client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": True},
    )
    client.put(
        "/api/recipes/recipe-002/favorite",
        json={"is_favorite": False},
    )

    response = client.get(
        "/api/recipes",
        params={"favorite": False},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"
    assert data[0]["is_favorite"] is False


def test_get_recipes_without_favorite_filter_returns_all_recipes() -> None:
    response = client.get("/api/recipes")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_favorite_filter_returns_empty_list_when_no_match() -> None:
    client.put(
        "/api/recipes/recipe-001/favorite",
        json={"is_favorite": False},
    )
    client.put(
        "/api/recipes/recipe-002/favorite",
        json={"is_favorite": False},
    )

    response = client.get(
        "/api/recipes",
        params={"favorite": True},
    )

    assert response.status_code == 200
    assert response.json() == []


def test_search_category_favorite_and_sort_recipes() -> None:
    client.put(
        "/api/recipes/recipe-002/favorite",
        json={"is_favorite": True},
    )

    response = client.get(
        "/api/recipes",
        params={
            "q": "Noodle",
            "category": "Noodles",
            "favorite": True,
            "sort": "title_asc",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == "recipe-002"
    assert data[0]["is_favorite"] is True