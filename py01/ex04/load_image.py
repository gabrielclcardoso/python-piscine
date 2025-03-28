from PIL import Image
import numpy as np
import sys


def ft_load(path: str) -> np.ndarray:
    """Loads image on the path, prints its shape and returns a 3d array
    representing each pixel as its RGB color
    """

    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

    arr = np.array(image)
    img = turn_to_greyscale(arr)
    return zoom_in(img)


def turn_to_greyscale(arr: np.ndarray) -> np.ndarray:
    """Receives an array representing an image and converts it to greyscale """

    image = Image.fromarray(arr)
    image = image.convert("L")

    return (np.array(image))


def zoom_in(img: np.ndarray) -> np.ndarray:
    """Receives an image and returns it zoomed in"""

    return img[105:505, 425:825]
