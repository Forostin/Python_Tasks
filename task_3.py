#За допомогою бібліотеки OpenCV об'єднати зображення green_rect.png i blue_triangle щоб фінальний результат виглядав як example.png.

import cv2
import numpy as np

green_rect = cv2.imread('images/green_rect.png', 1)
cv2.imshow('Result', green_rect)
cv2.waitKey(1000)

blue_triangle = cv2.imread('images/blue_triangle.png', 1)
cv2.imshow('Result', blue_triangle)
cv2.waitKey(1000)

#result_image = cv2.addWeighted (green_rect, 0.5,blue_triangle, 0.5, 0)

result_image = cv2.bitwise_and(green_rect, blue_triangle, mask = None)

cv2.imshow('Merged_image', result_image)
cv2.waitKey(3000)
cv2.destroyAllWindows()