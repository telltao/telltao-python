"""
本类用来处理图像
    https://github.com/telltao/Python-100-Days/blob/master/Day01-15/15.%E5%9B%BE%E5%83%8F%E5%92%8C%E5%8A%9E%E5%85%AC%E6%96%87%E6%A1%A3%E5%A4%84%E7%90%86.md
 pip install pillow

"""
from PIL import Image, ImageFilter


# 裁剪图像
def cutting_image():
    image = Image.open('../4_read_write_file/aa.jpg')
    rect = 80, 20, 310, 360
    image.crop(rect).show()


# 生成缩略图
def icon_image():
    image = Image.open('../4_read_write_file/aa.jpg')
    size = 128, 128
    image.thumbnail(size)
    image.show()


# 缩放图像
def scale_image():
    image1 = Image.open('../4_read_write_file/aa.jpg')
    image2 = Image.open('../4_read_write_file/bb.jpg')
    rect = 80, 20, 310, 360
    guido_head = image2.crop(rect)
    width, height = guido_head.size
    image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))


# 旋转图像
def rotation_image():
    image = Image.open('../4_read_write_file/aa.jpg')
    image.rotate(180).show()
    image.transpose(Image.FLIP_LEFT_RIGHT).show()


# 操作像素
def pixel_image():
    image = Image.open('../4_read_write_file/aa.jpg')
    for x in range(80, 300):
        for y in range(20, 350):
            image.putpixel((x, y), (128, 128, 128))
    image.show()

# 滤镜
def filter_image():
    image = Image.open('../4_read_write_file/aa.jpg')
    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    # 裁剪
    # cutting_image()
    # 缩略图
    # icon_image()
    # 缩放图像
    # scale_image()
    # 旋转图像
    # rotation_image()
    # 操作像素
    # pixel_image()
    # 滤镜
    filter_image()
