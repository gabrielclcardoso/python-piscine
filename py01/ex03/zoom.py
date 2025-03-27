from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    image = ft_load("animal.jpeg")
    if image is None:
        exit(1)
    print(image)

    image = turn_to_greyscale(image[105:505, 425:825])
    print(f"New shape after slicing: {image.shape}")
    print(image)

    plt.imshow(image, cmap="gray")
    plt.show()


def turn_to_greyscale(arr: np.ndarray) -> np.ndarray:
    """Receives an array representing an image and converts it to greyscale """

    image = Image.fromarray(arr)
    image = image.convert("L")

    return (np.array(image))


if __name__ == "__main__":
    main()
