import cv2

# Загрузка изображения с МРТ мозга
image = cv2.imread('mri_brain.jpg')

# Преобразование изображения в оттенки серого
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Создание окна для отображения изображения
cv2.namedWindow('МРТ мозга')

# Функция для применения выбранной цветовой схемы к выделенной области


def apply_color_options(image):
    if color_options == 'viridis':
        return cv2.applyColorMap(image, cv2.COLORMAP_VIRIDIS)
    elif color_options == 'plasma':
        return cv2.applyColorMap(image, cv2.COLORMAP_PLASMA)
    elif color_options == 'inferno':
        return cv2.applyColorMap(image, cv2.COLORMAP_INFERNO)
    elif color_options == 'magma':
        return cv2.applyColorMap(image, cv2.COLORMAP_MAGMA)
    else:
        return image

# Функция для обработки щелчков кнопок


def processing_buttons(event, x, y, flags, param):
    global color_options
    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 <= y <= 60:
            if 10 <= x <= 160:
                color_options = 'viridis'
            elif 170 <= x <= 320:
                color_options = 'plasma'
            elif 330 <= x <= 480:
                color_options = 'inferno'
            elif 490 <= x <= 640:
                color_options = 'magma'


# Установка функции обработки щелчков для окна с изображением
cv2.setMouseCallback('МРТ мозга', processing_buttons)

# Начальная цветовая схема - нет (исходное изображение в оттенках серого)
color_options = None

while True:
    # Применение выбранной цветовой схемы к изображению
    if color_options is not None:
        image = apply_color_options(grey_image)
    else:
        image = image

    # Отображение изображения с кнопками
    cv2.imshow('МРТ мозга', image)

    # Рисование кнопок в боковой части окна
    buttons = image.copy()
    cv2.rectangle(buttons, (10, 10), (160, 60), (255, 255, 255), -1)
    cv2.putText(buttons, 'Viridis', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(buttons, (170, 10), (320, 60), (255, 255, 255), -1)
    cv2.putText(buttons, 'Plasma', (180, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(buttons, (330, 10), (480, 60), (255, 255, 255), -1)
    cv2.putText(buttons, 'Inferno', (340, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(buttons, (490, 10), (640, 60), (255, 255, 255), -1)
    cv2.putText(buttons, 'Magma', (500, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('МРТ мозга', buttons)

    # Ожидание нажатия клавиши
    key = cv2.waitKey(1) & 0xFF

    # Нажмите 'q' для выхода из цикла
    if key == ord('q'):
        break

# Закрытие окна OpenCV
cv2.destroyAllWindows()