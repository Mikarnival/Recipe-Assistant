from fastapi import FastAPI

from app.data import RECIPES
from app.models import RecipeSummary

app = FastAPI(
    title="Recipe Assistant API",
)

@app.get(
    "/api/recipes",
    response_model=list[RecipeSummary],
)
def get_recipes() -> list[dict]:
    return RECIPES


