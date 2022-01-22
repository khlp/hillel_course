from PIL import Image, ImageDraw

# Создаем белый квадрат
img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(img)

idraw.rectangle((10, 10, 100, 100), fill='blue')

img.save('rectangle.png')