export function scaleQuantity(
  quantity: number,
  originalServings: number,
  preferredServings: number
): number {
  if (
    originalServings <= 0 ||
    preferredServings <= 0
  ) {
    return quantity
  }

  return (
    quantity *
    preferredServings /
    originalServings
  )
}