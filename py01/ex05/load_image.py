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
    print(f"The shape of the image is: {arr.shape}")
    print(arr)
    return arr
