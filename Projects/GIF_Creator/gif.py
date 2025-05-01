#This is a module used for reading and writing a wide variety of image, video, and scientific data formats
import imageio.v3 as iio 

# Path for the images
path = ['Projects\GIF_Creator\\team-pic1.png', 'Projects\GIF_Creator\\team-pic2.png']

# Readed data of the images are to be stored in a list
img = []

for filename in path:
    img.append(iio.imread(filename))

# Write an image to the specified file.
iio.imwrite('Projects\GIF_Creator\\image.gif', img, duration=500, loop=0)