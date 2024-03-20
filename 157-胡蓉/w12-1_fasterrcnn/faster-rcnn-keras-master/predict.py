from frcnn import FRCNN
from PIL import Image

frcnn = FRCNN()

while True:
    try:
        image = Image.open('img/street.jpg')
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = frcnn.detect_image(image)
        r_image.show()
frcnn.close_session()
    
