from PIL import Image, ImageDraw

# Create picture
img = Image.new('RGBA', (200, 200), 'white')
idraw = ImageDraw.Draw(img)

idraw.rectangle((10, 10, 100, 100), fill='blue')

img.save('rectangle.png')

# Change size
width = int(input("Input width: "))
height = int(input("Input height: "))
img = img.resize((width, height), Image.ANTIALIAS)
img.show()