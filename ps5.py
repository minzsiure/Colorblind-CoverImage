"""
# Problem Set 5
# Name: Eva Yi Xie
# Collaborators: N/A
# Time: 2 hours
"""    
from PIL import Image
import numpy

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0],[.558, .442, 0],[0, .242, .758]]
    elif color == 'green':
        c = [[0.625,0.375, 0],[ 0.7,0.3, 0],[0, 0.142,0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0],[0, 0.433, 0.567],[0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0],[0, 1, 0.],[0, 0., 1]]
    return c


def matrix_multiply(m1,m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1,m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    """
    Takes a filename (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of representing pixels.

    For RGB images, each pixel is a tuple containing (R,G,B) values.
    For BW images, each pixel is an integer.

    # Note: Don't worry about determining if an image is RGB or BW.
            The PIL library functions you use will return the 
            correct pixel values for either image mode.

    Returns the list of pixels.

    Inputs:
        filename: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values 
                 in form (R,G,B) such as [(0,0,0),(255,255,255),(38,29,58)...] for RGB image
                 in form L such as [60,66,72...] for BW image
    """
    inp = Image.open(filename)

    pixels = list(inp.getdata())
    
    return pixels





def pix_to_img(pixels, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of
                img_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """

    im = Image.new(mode, size)
    im.putdata(pixels)
    return im




def filter(pixels, color):
    """
    pixels: a list of pixels in RGB form, such as 
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """

    output= []
    c_m = make_matrix(color)
    temp = []
    for pixel in pixels: #for every tuple in pixel list
        
        m_mult = matrix_multiply(c_m, pixel) 
        
        for ele in m_mult:
            
            temp.append(int(ele))

        output.append((temp[0],temp[1],temp[2]))
        temp = []
                   
    return output




def extract_end_bits(num_bits, pixel):
    """
    Extracts the last num_bits bits of each value of a given pixel. 

    example for BW pixel:
        num_bits = 5
        pixel = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    example for RBG pixel:
        num_bits = 2
        pixel = (214, 17, 8)

        last 3 bits of 214 = 110 --> 6
        last 3 bits of 17 = 001 --> 1
        last 3 bits of 8 = 000 --> 0

        so we return (6,1,0)

    Inputs:
        num_bits: the number of bits to extract
        pixel: an integer between 0 and 255, or a tuple of RGB values between 0 and 255

    Returns:
        The last num_bits bits of pixel, as an integer (BW) or tuple of integers (RGB).
    """

    temp = []
    if type(pixel) == int: 
        return (pixel%(2**num_bits))
    
    else:
        for num in pixel:
            temp.append(num%(2**num_bits))
          
        return tuple(temp)

# num_bits = 3
# pixel = (214,17,8)
# print(extract_end_bits(num_bits, pixel))
    
        
def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    
    im = Image.open(filename) #import image
    width, height = im.size #generate size
    pixel = img_to_pix(filename) #generate pixel
    
    num_bits = 1 #single LSB
    
    temp = []
    for tup in pixel:
        temp.append(255*extract_end_bits(num_bits, tup)) 
                
    return pix_to_img(temp, (width, height), 'L') #generate image from pixel


# print(reveal_bw_image('hidden1.bmp'))

def reveal_color_image(filename):
    """
    Extracts the 2 LSBs for each pixel in the RGB input image. 
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    width, height = im.size
    pixel = img_to_pix(filename)
    
    num_bits = 2 #2 LSB
    
    temp = []
    output = []
    for tup in pixel:
        for num in tup:
            temp.append(85*extract_end_bits(num_bits, num))
        output.append(tuple(temp))
        temp = []

        
    return pix_to_img(output, (width, height), 'RGB')


    



def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 2 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """    
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def main():
    pass

    # Uncomment the following lines to test part 1

    # im = Image.open('image_15.png')
    # width, height = im.size
    # pixels = img_to_pix('image_15.png')

    # non_filtered_pixels = filter(pixels,'none')
    # im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    # im.show()

    # red_filtered_pixels = filter(pixels,'red')
    # im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')
    # im2.show()

    # # Uncomment the following lines to test part 2
    # im = reveal_image('hidden1.bmp')
    # im.show()
    
    # im2 = reveal_image('hidden2.bmp')
    # im2.show()


if __name__ == '__main__':
    main()

