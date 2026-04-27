import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _(mo, np):
    # Defining a tiny image using black (0), white (255) andd grey(0<x<255)
    # A tiny 3x3 image
    tiny_image = np.array([
        [0, 0, 0],
        [255, 128, 255],
        [0, 0, 0]
    ], dtype=np.uint8)

    tiny_image_widget = mo.ui.matrix(
        tiny_image,
        min_value=0,
        max_value=255,
        step=1,
        label="Image-Matrix Representation"
    )

    return (tiny_image_widget,)


@app.cell
def _(tiny_image_widget):
    # This is what the computer sees
    print("This is what the computer sees:")
    tiny_image_widget
    return


@app.cell
def _(plt, tiny_image_widget):
    # function for displaying image from the matrix

    def m2imshow(matrix, title="Our 3x3 matrix", axis_on_off='off', cmap='gray'):
        # Image of the matrix
        plt.imshow(matrix, cmap=cmap)
        plt.title(title)
        plt.axis(axis_on_off)
        plt.show()


    m2imshow(tiny_image_widget.value)
    return (m2imshow,)


@app.cell
def _(np, tiny_image_widget):
    image_pixel_values = np.array(tiny_image_widget.value)

    print(image_pixel_values, '\n\n')
    print("Top left corner pixel: ",image_pixel_values[0, 0])

    print("Center corner pixel: ",image_pixel_values[1, 1])
    return (image_pixel_values,)


@app.cell
def _(image_pixel_values, m2imshow):
    # Changing the value of a pixel

    image_pixel_values[1, 1] = 0
    print(image_pixel_values[1,1])

    m2imshow(image_pixel_values)
    return


@app.cell
def _(np):
    # Coloured matrix for demonstration
    # RGB - Each row column is like 3 spreadsheed stack on top of each other
    tiny_image_coloured = np.array([
        [[255, 0, 0], [0, 255, 0]],
        [[0, 0, 255], [0, 255, 169]]
    ], dtype=np.uint8)

    print(tiny_image_coloured)
    return (tiny_image_coloured,)


@app.cell
def _(m2imshow, tiny_image_coloured):
    m2imshow(tiny_image_coloured)
    return


if __name__ == "__main__":
    app.run()
