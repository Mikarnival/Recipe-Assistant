export {}
const API_BASE_URL = "http://127.0.0.1:8000"

let searchTimer: number | undefined

interface RecipeSummary {
  id: string
  title: string
  category: string
  servings: number
  is_favorite: boolean
}

interface RecipeQuery {
  q: string
  category: string
  sort: string
  favorite?: boolean
}

Page({
  data: {
    recipes: [] as RecipeSummary[],
    loading: false,
    error: "",
    searchTerm: "",
    selectedCategory: "",
    favoriteOnly: false,
    sortOption: "",
  },

  onShow() {
    this.loadRecipes()
  },

  onUnload() {
    if (searchTimer !== undefined) {
      clearTimeout(searchTimer)
    }
  },

  onSearchInput(event) {
    this.setData({
      searchTerm: event.detail.value
    })

    if (searchTimer !== undefined) {
      clearTimeout(searchTimer)
    }

    searchTimer = setTimeout(() => {
      this.loadRecipes()
    }, 300)
  },

  loadRecipes() {
    this.setData({
      loading: true,
      error: ""
    })

    const requestData: RecipeQuery = {
      q: this.data.searchTerm,
      category: this.data.selectedCategory,
      sort: this.data.sortOption,
    }

    if (this.data.favoriteOnly) {
      requestData.favorite = true
    }

    wx.request({
      url: `${API_BASE_URL}/api/recipes`,
      method: "GET",
      data: requestData,

      success: (response) => {
        if (response.statusCode === 200) {
          this.setData({
            recipes: response.data as RecipeSummary[],
            error: ""
          })

          return
        }

        this.setData({
          recipes: [],
          error: "Failed to load recipes"
        })
      },

      fail: () => {
        this.setData({
          recipes: [],
          error: "Failed to load recipes"
        })
      },

      complete: () => {
        this.setData({
          loading: false
        })
      }
    })
  },

  onCreateRecipeTap() {
    wx.navigateTo({
      url: "/pages/recipe-create/recipe-create",
    })
  },

  onRecipeTap(event) {
    const recipeId = event.currentTarget.dataset.recipeId

    wx.navigateTo({
      url: `/pages/recipe-detail/recipe-detail?id=${recipeId}`,
    })
  },

  onCategoryChange(event) {
    const category = event.currentTarget.dataset.category

    this.setData({
      selectedCategory: category
    })

    this.loadRecipes()
  },

  onFavoriteFilterChange() {
    this.setData({
      favoriteOnly: !this.data.favoriteOnly
    })

    this.loadRecipes()
  },

  onSortChange(event) {
    const sort = event.currentTarget.dataset.sort

    this.setData({
      sortOption: sort
    })

    this.loadRecipes()
  },

  onFavoriteTap(event) {
    const recipeId = event.currentTarget.dataset.recipeId
    const isFavorite = Boolean(
      event.currentTarget.dataset.isFavorite
    )

    wx.request({
      url: `${API_BASE_URL}/api/recipes/${recipeId}/favorite`,
      method: "PUT",

      data: {
        is_favorite: !isFavorite
      },

      success: (response) => {
        if (response.statusCode === 200) {
          this.loadRecipes()
          return
        }

        this.setData({
          error: "Failed to update favorite"
        })
      },

      fail: () => {
        this.setData({
          error: "Failed to update favorite"
        })
      }
    })
  },
  
  onSettingsTap() {
    wx.navigateTo({
      url: "/pages/settings/settings"
    })
  },
})