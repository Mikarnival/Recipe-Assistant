interface RecipeSummary {
  id: string
  title: string
  category: string
  servings: number
}

Page({
  data: {
    recipes: [] as RecipeSummary[],
    loading: false,
    error: ""
  },

  onLoad() {
    this.loadRecipes()
  },

  loadRecipes() {
    this.setData({
      loading: true,
      error: ""
    })

    wx.request({
      url: "http://127.0.0.1:8000/api/recipes",
      method: "GET",

      success: (response) => {
        this.setData({
          recipes: response.data as RecipeSummary[]
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to load recipes"
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