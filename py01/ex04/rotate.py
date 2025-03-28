from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def transpose(matrix: np.ndarray) -> np.ndarray:
    """Takes a square matrix and transposes it"""
    rows, cols = matrix.shape

    transposed = np.empty((rows, cols))
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = matrix[i, j]
    return transposed


def main():
    image = ft_load("animal.jpeg")
    if image is None:
        exit(1)
    print(f"The shape of image is: {image.shape}")
    print(image)

    image = transpose(image)
    print(f"New shape after transpose: {image.shape}")
    print(image)

    plt.imshow(image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
