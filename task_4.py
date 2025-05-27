# 4. Конвертувати test.pdf файл у зображення у форматі .png за допомогою бібліотеки pypdfium2 (або іншої) і зберегти результуюче зображення.

import pypdfium2 as pdfium
import cv2
import numpy as np

# Открываем PDF-документ
pdf = pdfium.PdfDocument("images/test.pdf")
n_pages = len(pdf)

for page_number in range(n_pages):
    page = pdf.get_page(page_number)

    # Создаём объект рендера
    bitmap = page.render(scale=1.0)
    
    # Получаем PIL-изображение
    pil_image = bitmap.to_pil()

    # Сохраняем изображение
    pil_image.save(f"new_images/image_{page_number + 1}.png")

    # Преобразуем в формат OpenCV
    image_cv = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGBA2BGR)

    # Показываем изображение
    cv2.imshow("Result_image", image_cv)
    cv2.waitKey(3000)

cv2.destroyAllWindows()
