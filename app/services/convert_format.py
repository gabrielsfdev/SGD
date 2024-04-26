# import pyheif
from PIL import Image
import numpy as np
import cv2
from pillow_heif import register_heif_opener

register_heif_opener()

def format_identificator(img_path):
    format = img_path[-3:]
    if img_path[-3:] == "jpg" or img_path[-3:] == "peg" or img_path[-3:] == "png" or img_path[-3:] == "EIC":
        # img = Image.fromarray(img)
        img = Image.open(img_path)
        # print("O formato é: ", img.format) # Apenas para debug
        if img.format == 'HEIC':
            return heic_to_BGR(img)
        elif img.format == 'PNG':
            return png_to_BGR(img)
        else:
            return np.array(img)
        

def heic_to_BGR(heif_file): # Precisa de um arquivo heic para testar
    # heif_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # cv2.imwrite('image.jpg', image) # Para salvar em jpg, não necessário por enquanto
    return image

def png_to_BGR(image):
    # image = cv2.imread(png_path)
    img = np.array(image)
    new_image = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    # cv2.imwrite('image.jpg', image) # Para salvar em jpg, não necessário por enquanto
    return new_image