import cv2
import os
print(os.listdir('./images/'))

folder_images = os.listdir('./images/')
for image in folder_images:
   if ".png" in image:
       print(image)
       png_image = cv2.imread(f"images/{image}")
       cv2.imshow('Result', png_image)
       cv2.waitKey(1000)

cv2.destroyAllWindows()







