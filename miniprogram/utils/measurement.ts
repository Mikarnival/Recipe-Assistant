export function convertVolume(
  quantity: number,
  sourceUnit: string,
  preferredUnit: string
): {
  quantity: number
  unit: string
} {
  if (sourceUnit === preferredUnit) {
    return {
      quantity,
      unit: sourceUnit
    }
  }

  if (
    sourceUnit === "ml" &&
    preferredUnit === "l"
  ) {
    return {
      quantity: quantity / 1000,
      unit: "l"
    }
  }

  if (
    sourceUnit === "l" &&
    preferredUnit === "ml"
  ) {
    return {
      quantity: quantity * 1000,
      unit: "ml"
    }
  }

  return {
    quantity,
    unit: sourceUnit
  }
}