from image import Image

def blur(img):
    blurred = Image.create(img.width, img.height, 0, img.max_value)
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
            neighbourhood = [
                img.get(row - 1, col - 1), img.get(row - 1, col), img.get(row - 1, col + 1),
                img.get(row, col - 1), img.get(row, col), img.get(row, col + 1),
                img.get(row + 1, col - 1), img.get(row + 1, col), img.get(row + 1, col + 1)
            ]
            average = sum(neighbourhood) // len(neighbourhood)
            blurred.set(row, col, average)
    return blurred