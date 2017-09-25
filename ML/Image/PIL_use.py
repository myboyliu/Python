'''
1）打开图像
'''

from PIL import Image
im = Image.open("E:/photoshop/1.jpg")

'''
2）读写图像
PIL 模块支持大量图片格式。使用在 Image 模块的 open() 函数从磁盘读取文件。你不需要知道文件格式就能打开它，这个库能够根据文件内容自动确定文件格式。要保存文件，使用 Image 类的 save() 方法。保存文件的时候文件名变得重要了。除非你指定格式，否则这个库将会以文件名的扩展名作为格式保存。
加载文件，并转化为png格式：
'''
from PIL import Image
import os
import sys

for infile in sys.argv[1:]:
    f,e = os.path.splitext(infile)
    outfile = f +".png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("Cannot convert", infile)

'''
3）创建缩略图
缩略图是网络开发或图像软件预览常用的一种基本技术，使用Python的Pillow图像库可以很方便的建立缩略图，如下：
'''
# create thumbnail
size = (128,128)
for infile in glob.glob("E:/photoshop/*.jpg"):
    f, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS)
    img.save(f+".thumbnail","JPEG")


'''
4）图像的剪切、粘贴与合并操作
Image 类包含的方法允许你操作图像部分选区，PIL.Image.Image.crop 方法获取图像的一个子矩形选区，如：
矩形选区有一个4元元组定义，分别表示左、上、右、下的坐标。这个库以左上角为坐标原点，单位是px，所以上诉代码复制了一个 200×200 pixels 的矩形选区。这个选区现在可以被处理并且粘贴到原图。	
'''
# crop, paste and merge
im = Image.open("E:/photoshop/lena.jpg")
box = (100,100,300,300)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)



'''
5）分离和合并颜色通道
对于多通道图像，有时候在处理时希望能够分别对每个通道处理，处理完成后重新合成多通道，在Pillow中，很简单，如下：
'''
r,g,b = im.split()
im = Image.merge("RGB", (r,g,b))


'''
 6）几何变换
对图像进行几何变换是一种基本处理，在Pillow中包括resize( )和rotate( )，如用法如下：
其中，resize( )函数的参数是一个新图像大小的元祖，而rotate( )则需要输入顺时针的旋转角度。在Pillow中，对于一些常见的旋转作了专门的定义：
'''
out = im.resize((128,128))
out = im.rotate(45)  # degree conter-clockwise
	
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)

'''
7）颜色空间变换
在处理图像时，根据需要进行颜色空间的转换，如将彩色转换为灰度：
'''
cmyk = im.convert("CMYK")
gray = im.convert("L")
binary = im.convert("1")
rgb = im.convert("RGB")

'''
8）图像滤波
图像滤波在ImageFilter 模块中，在该模块中，预先定义了很多增强滤波器，可以通过filter( )函数使用，预定义滤波器包括：
BLUR、CONTOUR、DETAIL、EDGE_ENHANCE、EDGE_ENHANCE_MORE、EMBOSS、FIND_EDGES、SMOOTH、SMOOTH_MORE、SHARPEN。其中BLUR就是均值滤波，CONTOUR找轮廓，FIND_EDGES边缘检测，使用该模块时，需先导入，使用方法如下：
'''
from PIL import ImageFilter

imgF = Image.open("E:/photoshop/lena.jpg")
outF = imgF.filter(ImageFilter.DETAIL)
conF = imgF.filter(ImageFilter.CONTOUR)
edgeF = imgF.filter(ImageFilter.FIND_EDGES)
imgF.show()
outF.show()
conF.show()
edgeF.show()

