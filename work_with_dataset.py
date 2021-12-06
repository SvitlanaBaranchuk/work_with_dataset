# import of necessary libraries and modules
from PIL import Image, ImageDraw


def draw(name_file, name_image, size):
    # create a picture
    img = Image.new("RGB", size, "white")
    # in order to draw a picture, create an ImageDraw object and pass it a picture
    dr = ImageDraw.Draw(img)

    # open the dataset
    dataset = open(name_file, "r")

    # display points at given coordinates
    for coordinates in dataset:
        dr.point((int(coordinates[3:]), int(coordinates[:3])), fill = "black")

    # show the picture
    img.show()
    # save the image in PNG format
    img.save(name_image, "PNG")


draw("DS1.txt", "result.png", (960, 540))