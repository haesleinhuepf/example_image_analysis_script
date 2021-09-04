from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label

def segment_image(image):
    # denoise the image
    blurred = gaussian(image, sigma=2)

    # binarize the image
    binary = threshold_otsu(blurred)
    
    # label connected components
    result = label(binary)

    return result
