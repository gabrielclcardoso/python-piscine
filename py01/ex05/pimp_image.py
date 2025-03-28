import matplotlib.pyplot as plt
from load_image import ft_load
from numpy import ndarray as array


def ft_invert(array) -> array:
    """Inverts the color of the image received."""

    return (255 - array)


def ft_red(array) -> array:
    """Turns image red"""

    array[:, :, 1] = 0
    array[:, :, 2] = 0

    return array


def ft_green(array) -> array:
    """Turns image green"""

    array[:, :, 0] = 0
    array[:, :, 2] = 0

    return array


def ft_blue(array) -> array:
    """Turns image blue"""

    array[:, :, 0] = 0
    array[:, :, 1] = 0

    return array


def ft_grey(array) -> array:
    """Turns image grey"""

    array[:, :, 0] = array[:, :, 1]
    array[:, :, 2] = array[:, :, 1]

    return array


# def main():
#     imgs = []
#
#     image = ft_load("landscape.jpg")
#     if image is None:
#         exit(1)
#
#     imgs.append(image)
#     imgs.append(ft_invert(image.copy()))
#     imgs.append(ft_red(image.copy()))
#     imgs.append(ft_green(image.copy()))
#     imgs.append(ft_blue(image.copy()))
#     imgs.append(ft_grey(image.copy()))
#
#     for i in imgs:
#         plt.figure()
#         plt.imshow(i)
#         plt.show()
#
#
# if __name__ == "__main__":
#     main()
