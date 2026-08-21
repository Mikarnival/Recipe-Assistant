export {}

const API_BASE_URL = "http://127.0.0.1:8000"

interface IngredientFormItem {
  name: string
  quantity: string
  unit: string
  unitIndex: number
}

interface StepFormItem {
  instruction: string
}

interface RecipeCreateRequest {
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

    servings: "2",

    units: [
      "g",
      "kg",
      "ml",
      "l",
      "piece",
      "tbsp",
      "tsp",
    ],

    ingredients: [
      {
        name: "",
        quantity: "",
        unit: "",
        unitIndex: -1,
      }
    ] as IngredientFormItem[],

    preparationTasks: [
      ""
    ],

    steps: [
      {
        instruction: "",
      }
    ] as StepFormItem[],

    submitting: false,
    error: "",
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
    const ingredients = [
      ...this.data.ingredients,
      {
        name: "",
        quantity: "",
        unit: "",
        unitIndex: -1,
      }
    ]

    this.setData({
      ingredients
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
    const steps = [
      ...this.data.steps,
      {
        instruction: "",
      }
    ]

    this.setData({
      steps
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

  buildRequestData(): RecipeCreateRequest {
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

  onSubmit() {
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
      url: `${API_BASE_URL}/api/recipes`,
      method: "POST",
      data: requestData,

      success: (response) => {
        if (response.statusCode === 201) {
          wx.showToast({
            title: "Recipe created",
            icon: "success",
          })

          wx.navigateBack()

          return
        }

        this.setData({
          error: "Failed to create recipe."
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to create recipe."
        })
      },

      complete: () => {
        this.setData({
          submitting: false
        })
      }
    })
  },
})