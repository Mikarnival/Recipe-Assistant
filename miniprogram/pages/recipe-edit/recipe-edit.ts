export {}

const API_BASE_URL = "http://127.0.0.1:8000"

interface Ingredient {
  name: string
  quantity: number
  unit: string
}

interface CookingStep {
  instruction: string
}

interface RecipeDetail {
  id: string
  title: string
  category: string
  servings: number
  is_favorite: boolean
  ingredients: Ingredient[]
  preparation_tasks: string[]
  steps: CookingStep[]
}

interface IngredientFormItem {
  name: string
  quantity: string
  unit: string
  unitIndex: number
}

interface StepFormItem {
  instruction: string
}

interface RecipeUpdateRequest {
  title: string
  category: string
  servings: number
  ingredients: {
    name: string
    quantity: number
    unit: string
  }[]
  preparation_tasks: string[]
  steps: {
    instruction: string
  }[]
}

Page({
  data: {
    recipeId: "",

    title: "",

    category: "",
    categories: [
      "Chinese",
      "Noodles",
      "Soup",
      "Rice",
      "Meat",
      "Vegetable",
      "Dessert",
      "Other",
    ],
    selectedCategoryIndex: -1,

    servings: "",

    units: [
      "g",
      "kg",
      "ml",
      "l",
      "piece",
      "tbsp",
      "tsp",
    ],

    ingredients: [] as IngredientFormItem[],

    preparationTasks: [] as string[],

    steps: [] as StepFormItem[],

    loading: false,
    submitting: false,
    error: "",
  },

  onLoad(options) {
    const recipeId = options.id

    if (!recipeId) {
      this.setData({
        error: "Recipe ID is missing."
      })

      return
    }

    this.setData({
      recipeId
    })

    this.loadRecipe()
  },

  loadRecipe() {
    this.setData({
      loading: true,
      error: ""
    })

    wx.request({
      url: `${API_BASE_URL}/api/recipes/${this.data.recipeId}`,
      method: "GET",

      success: (response) => {
        if (response.statusCode === 200) {
          const recipe = response.data as RecipeDetail

          const selectedCategoryIndex =
            this.data.categories.indexOf(recipe.category)

          const ingredients = recipe.ingredients.map(
            (ingredient) => ({
              name: ingredient.name,
              quantity: String(ingredient.quantity),
              unit: ingredient.unit,
              unitIndex: this.data.units.indexOf(ingredient.unit),
            })
          )

          const preparationTasks =
            recipe.preparation_tasks.length > 0
              ? [...recipe.preparation_tasks]
              : [""]

          const steps = recipe.steps.map(
            (step) => ({
              instruction: step.instruction,
            })
          )

          this.setData({
            title: recipe.title,
            category: recipe.category,
            selectedCategoryIndex,
            servings: String(recipe.servings),
            ingredients,
            preparationTasks,
            steps,
            error: "",
          })

          return
        }

        if (response.statusCode === 404) {
          this.setData({
            error: "Recipe not found."
          })

          return
        }

        this.setData({
          error: "Failed to load recipe."
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to load recipe."
        })
      },

      complete: () => {
        this.setData({
          loading: false
        })
      }
    })
  },

  onTitleInput(event) {
    this.setData({
      title: event.detail.value
    })
  },

  onCategoryChange(event) {
    const selectedCategoryIndex = Number(event.detail.value)
    const category = this.data.categories[selectedCategoryIndex]

    this.setData({
      selectedCategoryIndex,
      category,
    })
  },

  onServingsInput(event) {
    this.setData({
      servings: event.detail.value
    })
  },

  onIngredientNameInput(event) {
    const index = event.currentTarget.dataset.index

    this.setData({
      [`ingredients[${index}].name`]: event.detail.value
    })
  },

  onIngredientQuantityInput(event) {
    const index = event.currentTarget.dataset.index

    this.setData({
      [`ingredients[${index}].quantity`]: event.detail.value
    })
  },

  onIngredientUnitChange(event) {
    const index = event.currentTarget.dataset.index
    const unitIndex = Number(event.detail.value)
    const unit = this.data.units[unitIndex]

    this.setData({
      [`ingredients[${index}].unit`]: unit,
      [`ingredients[${index}].unitIndex`]: unitIndex,
    })
  },

  addIngredient() {
    this.setData({
      ingredients: [
        ...this.data.ingredients,
        {
          name: "",
          quantity: "",
          unit: "",
          unitIndex: -1,
        }
      ]
    })
  },

  removeIngredient(event) {
    const index = event.currentTarget.dataset.index

    if (this.data.ingredients.length === 1) {
      return
    }

    const ingredients = this.data.ingredients.filter(
      (_, ingredientIndex) => ingredientIndex !== index
    )

    this.setData({
      ingredients
    })
  },

  onPreparationTaskInput(event) {
    const index = event.currentTarget.dataset.index

    this.setData({
      [`preparationTasks[${index}]`]: event.detail.value
    })
  },

  addPreparationTask() {
    this.setData({
      preparationTasks: [
        ...this.data.preparationTasks,
        ""
      ]
    })
  },

  removePreparationTask(event) {
    const index = event.currentTarget.dataset.index

    const preparationTasks = this.data.preparationTasks.filter(
      (_, taskIndex) => taskIndex !== index
    )

    if (preparationTasks.length === 0) {
      preparationTasks.push("")
    }

    this.setData({
      preparationTasks
    })
  },

  onStepInstructionInput(event) {
    const index = event.currentTarget.dataset.index

    this.setData({
      [`steps[${index}].instruction`]: event.detail.value
    })
  },

  addStep() {
    this.setData({
      steps: [
        ...this.data.steps,
        {
          instruction: "",
        }
      ]
    })
  },

  removeStep(event) {
    const index = event.currentTarget.dataset.index

    if (this.data.steps.length === 1) {
      return
    }

    const steps = this.data.steps.filter(
      (_, stepIndex) => stepIndex !== index
    )

    this.setData({
      steps
    })
  },

  validateForm(): string | null {
    if (!this.data.title.trim()) {
      return "Recipe title is required."
    }

    if (!this.data.category.trim()) {
      return "Category is required."
    }

    const servings = Number(this.data.servings)

    if (
      !Number.isInteger(servings)
      || servings <= 0
    ) {
      return "Servings must be a positive whole number."
    }

    for (const ingredient of this.data.ingredients) {
      if (!ingredient.name.trim()) {
        return "Each ingredient must have a name."
      }

      const quantity = Number(ingredient.quantity)

      if (
        !Number.isFinite(quantity)
        || quantity <= 0
      ) {
        return "Each ingredient must have a positive quantity."
      }

      if (!ingredient.unit.trim()) {
        return "Each ingredient must have a unit."
      }
    }

    for (const step of this.data.steps) {
      if (!step.instruction.trim()) {
        return "Each cooking step must contain an instruction."
      }
    }

    return null
  },

  buildRequestData(): RecipeUpdateRequest {
    return {
      title: this.data.title.trim(),
      category: this.data.category.trim(),
      servings: Number(this.data.servings),

      ingredients: this.data.ingredients.map(
        (ingredient) => ({
          name: ingredient.name.trim(),
          quantity: Number(ingredient.quantity),
          unit: ingredient.unit.trim(),
        })
      ),

      preparation_tasks: this.data.preparationTasks
        .map((task) => task.trim())
        .filter((task) => task.length > 0),

      steps: this.data.steps.map(
        (step) => ({
          instruction: step.instruction.trim(),
        })
      ),
    }
  },

  onSave() {
    if (this.data.submitting) {
      return
    }

    const validationError = this.validateForm()

    if (validationError !== null) {
      this.setData({
        error: validationError
      })

      return
    }

    const requestData = this.buildRequestData()

    this.setData({
      submitting: true,
      error: ""
    })

    wx.request({
      url: `${API_BASE_URL}/api/recipes/${this.data.recipeId}`,
      method: "PUT",
      data: requestData,

      success: (response) => {
        if (response.statusCode === 200) {
          wx.showToast({
            title: "Recipe updated",
            icon: "success",
          })

          wx.navigateBack()

          return
        }

        if (response.statusCode === 404) {
          this.setData({
            error: "Recipe not found."
          })

          return
        }

        this.setData({
          error: "Failed to update recipe."
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to update recipe."
        })
      },

      complete: () => {
        this.setData({
          submitting: false
        })
      }
    })
  },

  onCancel() {
    wx.navigateBack()
  },
})