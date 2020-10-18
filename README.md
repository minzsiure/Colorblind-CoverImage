# Colorblind-CoverImage
Make use of Python’s Image Library and matrix multiplication to 1) create images for testing colorblind, and 2) recover coded image!


1)
The human eye contains two types of photoreceptive (light sensitive) cells: rods and cones. Rods are responsible for vision in low light environments, such as at night, and cones are responsible for color vision. There are three types of cones, each responsible for a particular color, that is, red, green and blue. The red, green and blue cones all work together allowing you to see the whole spectrum of colors. For example, when the red and blue cones are stimulated in a certain way, you will see the color purple.

The condition known as colorblindness typically manifests as a deficiency in one of these types of cones, for example, protanopia is a lack of sensitivity to red light, so the following is an example of the difference in viewing an image.

The objective of this part is to create filters to simulate these differences. To do this, we will make use of Python’s Image Library or PIL for short. From PIL we will import Image, which is a sublibrary, or a set of functions and methods, related to image processing. With Image, we can convert images to a list of pixels, and manipulate the RGB (red, green, blue) values of these pixels.

We can replicate the effects of colorblindness with a matrix multiplication between a colorblindness transformation matrix and the RGB values of a particular pixel, which are represented as a vector with 3 entries.

You do not need to know anything about matrix multiplication; however, if you wish to pursue more information on it, see here.

Here is a general breakdown of the image transformation process:

Open the image in Python
Retrieve a list (of tuples or ints) of the pixel information
Iterate through pixels and multiply them by the transformation matrix using matrix_multiply
Save transformed pixels as an image


2) Hidden Messages in Images
In an image, it is possible to hide a second (secret) image that can only be recovered by certain mathematical operations. This is known as steganography. In this section, you will go through some examples and write your own steganography module to hide images.

In a black and white image, each pixel is represented by a numerical value that indicates its brightness. The minimum value for each pixel is 0 (which corresponds to black), while the maximum value (which corresponds to white) depends on the number of bits used for each pixel. In our examples, we will use 8-bit images. This means the pixels can take values between 0 and 255, inclusive (can you see why?).
