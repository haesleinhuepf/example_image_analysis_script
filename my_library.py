from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label

def segment_image(image):
    # denoise the image
    blurred = gaussian(image, sigma=2)

    # binarize the image
    threshold = threshold_otsu(blurred)
    binary = blurred > threshold
    
    # label connected components
    result = label(binary)

    return result
