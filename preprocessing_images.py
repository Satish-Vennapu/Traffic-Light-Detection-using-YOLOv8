# For the making the model robust and better prediction in different environment conditions
import cv2
import os
import numpy as np
import imgaug.augmenters as iaa

directory = 'path/to/images'
image_files = [file for file in os.listdir(directory) if file.endswith(('.jpg', '.png', '.jpeg'))]
images = []
    
for i, file in enumerate(image_files):
    image_path = os.path.join(directory, file)
    img = cv2.imread(image_path)

    # Flipping
    flipped_img = cv2.flip(img, 1) # Horizontal flip

    # Scaling and blur
    rs_img = cv2.resize(flipped_img, None, fx=0.2, fy=0.2, interpolation = cv2.INTER_LINEAR) 
    rs_img =cv2.GaussianBlur(rs_img)

    # Salt and Pepper noise
    sp_noise = iaa.SaltAndPepper(0.05) # 5% of pixels will be changed
    sp_img = sp_noise.augment_image(rs_img)

    # Contrast adjustment
    contrast = iaa.GammaContrast(gamma=2.0) # Gamma > 1 will darken the image
    contrast_img = contrast.augment_image(sp_img)
    

    # Saving the image
    cv2.imwrite(f"image{i}.jpg", sp_img)

# Display the images
# cv2.imshow('Original', img)
# cv2.imshow('Flipped', flipped_img)
# cv2.imshow('Scaled', res)
# cv2.imshow('Salt and Pepper noise', sp_img)
# cv2.imshow('Contrast adjustment', contrast_img)

cv2.waitKey(0)
cv2.destroyAllWindows()