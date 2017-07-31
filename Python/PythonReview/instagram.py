from PIL import Image

def getRed(pixel):
    return pixel[0]
def getGreen(pixel):
    return pixel[1]
def getBlue(pixel):
    return pixel[2]
def getAveragePixel(pixel):
    average = ((getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3)
    avg_pixel = (average, average, average)
    return avg_pixel

jpg = Image.open("cosmo.jpg")

print jpg.getdata()[200]

new_pixels = []
size = jpg.height * jpg.width
old_pixels = jpg.getdata()
for i in range(size):
    old_pixel = old_pixels[i]
    if ((i % jpg.width) > (jpg.width / 2)):
        new_pixel = getAveragePixel(old_pixel)
    else:
        new_pixel = old_pixel
    new_pixels.append(new_pixel)

# for pixel in jpg.getdata():
#     red_value = getRed(pixel)
#     green_value = getGreen(pixel)
#     blue_value = getBlue(pixel)
#     new_pixel = (red_value * 3, green_value * 3, blue_value * 3)
#     #new_pixels.append(getAveragePixel(pixel))
#     new_pixels.append(new_pixel)

print new_pixels[200]
new_image = Image.new("RGB", jpg.size)
new_image.putdata(new_pixels)
new_image.show()
new_image.save("newcosmo.jpg")
