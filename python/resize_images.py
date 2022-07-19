# Import packages
import cv2
import os
import glob
import numpy as np


folder = '/Users/chalexander/Desktop/Images'

for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))

    if img is not None:

        # Cropping an image
        cropped_image = img[89:345, 25:281]

        print(cropped_image.shape)
        cv2.imwrite(f"/Users/chalexander/Desktop/Cropped_Images/cropped_{filename}", cropped_image)
        cv2.imshow('image', cropped_image)
        cv2.waitKey(20)
        cv2.destroyAllWindows()


