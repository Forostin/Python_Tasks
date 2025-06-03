# 5. Порахувати загальну кількість фігур на зображенні figures.png 
# 	-намалювати зелені рамки для фігур, площа яких перевищує 2000 пікселів
# 	-заповнити червоним кольором (cv2.drawContours з аргументом thickness=cv2.FILLED) фігури, що мають менше 5 кутів
# 	-вивести отримане зображення на екран до натискання клавіші "q"

import cv2
import numpy as np
import keyboard

image = cv2.imread("images/figures.png")

if image is None:
    print("Не вдалося завантажити зображення!")
    exit()
else: cv2.imshow("Зображення ", image) 
cv2.waitKey(0) 

# Переводим в черно-белый формат
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Зображення чорно-білє", gray)  
cv2.waitKey(0) 


# Делаем размытие
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Зображення розмитє", blurred )  
cv2.waitKey(0) 


# выделяем контуры 
edged = cv2.Canny(blurred, 35, 125)  
cv2.imshow("Зображення ", edged )  
cv2.waitKey(0)

# Найти контуры
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# количество контуров (фигур)
num_figures = len(contours)

# Вивести результат
print(f"Загальна кількість фігур на зображенні: {num_figures}")

# (Опціонально) Показати зображення з контурами (для перевірки)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # Вималювати контури

while True :
    cv2.imshow("Зображення з контурами", image)  # Показати зображення
    if keyboard.is_pressed("q"):
        break
    cv2.waitKey(0)  # Чекати натискання клавіші "q"


cv2.destroyAllWindows()