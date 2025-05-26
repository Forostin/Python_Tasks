#2. Для зображення figures.png виконати наступні дії:
#	- зменшити його розмір до 1000х500 пікселів
#	- повернути зменшене зображення на 90 градусів за годинниковою стрілкою і зберегти результуюче зображення під назвою result.png

import cv2

figures = cv2.imread('images/figures.png')
cv2.imshow('Result', figures)
cv2.waitKey(3000)
print(figures.shape)

figures = cv2.resize(figures, (1000, 500))

# вычислим центр изображения
(h, w) = figures.shape[:2]
center = (w / 2, h / 2)
# повернем изображение на 90 градусов
M = cv2.getRotationMatrix2D(center, -90, 0.5)
rotated = cv2.warpAffine(figures, M, (w, h))
cv2.imshow("Rotated image", rotated)
cv2.waitKey(3000)

print(figures.shape)

cv2.imwrite('images/result.png', rotated)
cv2.destroyAllWindows()
