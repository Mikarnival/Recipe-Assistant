from __future__ import annotations

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    servings: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_favorite: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    ingredients: Mapped[list["Ingredient"]] = relationship(
        back_populates="recipe",
        cascade="all, delete-orphan",
        order_by="Ingredient.position",
    )

    preparation_tasks: Mapped[list["PreparationTask"]] = relationship(
        back_populates="recipe",
        cascade="all, delete-orphan",
        order_by="PreparationTask.position",
    )

    steps: Mapped[list["CookingStep"]] = relationship(
        back_populates="recipe",
        cascade="all, delete-orphan",
        order_by="CookingStep.position",
    )


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    recipe_id: Mapped[str] = mapped_column(
        ForeignKey("recipes.id"),
        nullable=False,
        index=True,
    )

    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    unit: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    recipe: Mapped["Recipe"] = relationship(
        back_populates="ingredients",
    )


class PreparationTask(Base):
    __tablename__ = "preparation_tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    recipe_id: Mapped[str] = mapped_column(
        ForeignKey("recipes.id"),
        nullable=False,
        index=True,
    )

    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    instruction: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    recipe: Mapped["Recipe"] = relationship(
        back_populates="preparation_tasks",
    )


class CookingStep(Base):
    __tablename__ = "cooking_steps"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    recipe_id: Mapped[str] = mapped_column(
        ForeignKey("recipes.id"),
        nullable=False,
        index=True,
    )

    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    instruction: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    recipe: Mapped["Recipe"] = relationship(
        back_populates="steps",
    )