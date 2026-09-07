import {
  DEFAULT_PREFERENCES,
  SpoonProfile,
  UserPreferences,
  loadPreferences,
  savePreferences
} from "../../utils/preferences"

Page({
  data: {
    preferences: DEFAULT_PREFERENCES as UserPreferences,

    tasteOptions: [
      "light",
      "normal",
      "strong"
    ],

    unitOptions: [
      "ml",
      "l"
    ],

    newSpoonName: "",
    newSpoonVolume: "",

    saveMessage: ""
  },

  onLoad() {
    this.setData({
      preferences: loadPreferences()
    })
  },

  onTastePreferenceChange(event) {
    const index = Number(event.detail.value)

    this.setData({
      "preferences.tastePreference":
        this.data.tasteOptions[index]
    })
  },

  onMeasurementUnitChange(event) {
    const index = Number(event.detail.value)

    this.setData({
      "preferences.measurementUnit":
        this.data.unitOptions[index]
    })
  },

  onDefaultServingsInput(event) {
    this.setData({
      "preferences.defaultServings":
        Number(event.detail.value)
    })
  },

  onSpoonNameInput(event) {
    this.setData({
      newSpoonName: event.detail.value
    })
  },

  onSpoonVolumeInput(event) {
    this.setData({
      newSpoonVolume: event.detail.value
    })
  },

  onAddSpoonTap() {
    const name = this.data.newSpoonName.trim()
    const volume = Number(this.data.newSpoonVolume)

    if (!name || volume <= 0) {
      wx.showToast({
        title: "Invalid spoon profile",
        icon: "none"
      })

      return
    }

    const newProfile: SpoonProfile = {
      id: `spoon-${Date.now()}`,
      name,
      volumeMl: volume
    }

    this.setData({
      "preferences.spoonProfiles": [
        ...this.data.preferences.spoonProfiles,
        newProfile
      ],

      newSpoonName: "",
      newSpoonVolume: ""
    })
  },

  onDeleteSpoonTap(event) {
    const spoonId = event.currentTarget.dataset.id

    this.setData({
      "preferences.spoonProfiles":
        this.data.preferences.spoonProfiles.filter(
          spoon => spoon.id !== spoonId
        )
    })
  },

  onSaveTap() {
    const preferences = this.data.preferences

    if (
      !Number.isInteger(preferences.defaultServings) ||
      preferences.defaultServings <= 0
    ) {
      wx.showToast({
        title: "Invalid serving size",
        icon: "none"
      })

      return
    }

    const saved = savePreferences(preferences)

    if (!saved) {
      this.setData({
        saveMessage: "Failed to save preferences"
      })

      return
    }

    this.setData({
      saveMessage: "Preferences saved"
    })

    wx.showToast({
      title: "Saved",
      icon: "success"
    })
  },

  onEditSpoonTap(event) {
    const spoonId = event.currentTarget.dataset.id

    const spoon = this.data.preferences.spoonProfiles.find(
      item => item.id === spoonId
    )

    if (!spoon) {
      return
    }

    this.setData({
      newSpoonName: spoon.name,
      newSpoonVolume: String(spoon.volumeMl)
    })

    this.onDeleteSpoonTap(event)
  },

  onSettingsTap() {
    wx.navigateTo({
      url: "/pages/settings/settings"
    })
  }
})