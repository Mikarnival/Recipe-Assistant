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
  ingredients: Ingredient[]
  preparation_tasks: string[]
  steps: CookingStep[]
}

Page({
  data: {
    recipe: null as RecipeDetail | null,
    loading: false,
    error: ""
  },

  onLoad(options) {
    const recipeId = options.id

    this.setData({
      loading: true,
      error:""
    })

    wx.request({
      url: `http://127.0.0.1:8000/api/recipes/${recipeId}`,
      method: "GET",

      success: (response) => {
        if (response.statusCode===200) {
          this.setData({
            recipe: response.data as RecipeDetail
          })
        } else if (response.statusCode===404){
          this.setData({
            error: "Recipe not found"
          })
        }
      },

      fail: () => {
        this.setData({
          error: "Failed to load recipe"
        })
      },

      complete: () => {
        this.setData({
          loading: false
        })
      }
    })
  }
})