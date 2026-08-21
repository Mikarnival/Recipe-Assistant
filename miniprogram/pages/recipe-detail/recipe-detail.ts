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

Page({
  data: {
    recipeId: "",
    recipe: null as RecipeDetail | null,
    loading: false,
    deleting: false,
    error: ""
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
  },

  onShow() {
    if (this.data.recipeId) {
      this.loadRecipe()
    }
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
          this.setData({
            recipe: response.data as RecipeDetail,
            error: ""
          })

          return
        }

        if (response.statusCode === 404) {
          this.setData({
            recipe: null,
            error: "Recipe not found"
          })

          return
        }

        this.setData({
          recipe: null,
          error: "Failed to load recipe"
        })
      },

      fail: () => {
        this.setData({
          recipe: null,
          error: "Failed to load recipe"
        })
      },

      complete: () => {
        this.setData({
          loading: false
        })
      }
    })
  },

  onEditRecipeTap() {
    wx.navigateTo({
      url: `/pages/recipe-edit/recipe-edit?id=${this.data.recipeId}`,
    })
  },

  onDeleteRecipeTap() {
    if (this.data.deleting) {
      return
    }

    wx.showModal({
      title: "Delete Recipe",
      content: "Are you sure you want to delete this recipe?",
      confirmText: "Delete",
      confirmColor: "#c62828",

      success: (result) => {
        if (result.confirm) {
          this.deleteRecipe()
        }
      }
    })
  },

  deleteRecipe() {
    this.setData({
      deleting: true,
      error: ""
    })

    wx.request({
      url: `${API_BASE_URL}/api/recipes/${this.data.recipeId}`,
      method: "DELETE",

      success: (response) => {
        if (response.statusCode === 204) {
          wx.showToast({
            title: "Recipe deleted",
            icon: "success",
          })

          wx.navigateBack()

          return
        }

        if (response.statusCode === 404) {
          this.setData({
            error: "Recipe not found"
          })

          return
        }

        this.setData({
          error: "Failed to delete recipe"
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to delete recipe"
        })
      },

      complete: () => {
        this.setData({
          deleting: false
        })
      }
    })
  },
})