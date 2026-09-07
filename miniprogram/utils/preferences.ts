export interface SpoonProfile {
  id: string
  name: string
  volumeMl: number
}

export interface UserPreferences {
  spoonProfiles: SpoonProfile[]
  tastePreference: string
  measurementUnit: string
  defaultServings: number
}

const STORAGE_KEY = "userPreferences"

export const DEFAULT_PREFERENCES: UserPreferences = {
  spoonProfiles: [],
  tastePreference: "normal",
  measurementUnit: "ml",
  defaultServings: 2
}

export function loadPreferences(): UserPreferences {
  try {
    const saved = wx.getStorageSync(STORAGE_KEY)

    if (!saved) {
      return DEFAULT_PREFERENCES
    }

    return {
      ...DEFAULT_PREFERENCES,
      ...saved
    }
  } catch {
    return DEFAULT_PREFERENCES
  }
}

export function savePreferences(
  preferences: UserPreferences
): boolean {
  try {
    wx.setStorageSync(STORAGE_KEY, preferences)
    return true
  } catch {
    return false
  }
}