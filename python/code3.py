from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

"""
# 图片缩放操作
# 打开一张图片
img = Image.open('test.jpg')
filename = img.filename.split('.')[0]
# 获取图像尺寸
w, h = img.size
print('原始图像的宽是:%s,高是%s' % (w, h))
# 缩放到50%
img.thumbnail((w // 2, h // 2))
print('缩放后的图像的宽是:%s,高是%s' % (w // 2, h // 2))
# 保存缩放后的图像
img.save('%s_thumbnail.jpg' % (filename,), 'jpeg')

# 模糊效果
img_2 = img.filter(ImageFilter.DETAIL)
img_2.save('blur.jpg', 'jpeg')
"""


def random_char():
    return chr(random.randint(65, 90))


def random_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def random_color2():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('/Library/Fonts/Silom.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=random_color())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), random_char(), font=font, fill=random_color2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')