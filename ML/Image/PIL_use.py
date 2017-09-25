'''
1����ͼ��
'''

from PIL import Image
im = Image.open("E:/photoshop/1.jpg")

'''
2����дͼ��
PIL ģ��֧�ִ���ͼƬ��ʽ��ʹ���� Image ģ��� open() �����Ӵ��̶�ȡ�ļ����㲻��Ҫ֪���ļ���ʽ���ܴ�����������ܹ������ļ������Զ�ȷ���ļ���ʽ��Ҫ�����ļ���ʹ�� Image ��� save() �����������ļ���ʱ���ļ��������Ҫ�ˡ�������ָ����ʽ����������⽫�����ļ�������չ����Ϊ��ʽ���档
�����ļ�����ת��Ϊpng��ʽ��
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
3����������ͼ
����ͼ�����翪����ͼ�����Ԥ�����õ�һ�ֻ���������ʹ��Python��Pillowͼ�����Ժܷ���Ľ�������ͼ�����£�
'''
# create thumbnail
size = (128,128)
for infile in glob.glob("E:/photoshop/*.jpg"):
    f, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS)
    img.save(f+".thumbnail","JPEG")


'''
4��ͼ��ļ��С�ճ����ϲ�����
Image ������ķ������������ͼ�񲿷�ѡ����PIL.Image.Image.crop ������ȡͼ���һ���Ӿ���ѡ�����磺
����ѡ����һ��4ԪԪ�鶨�壬�ֱ��ʾ���ϡ��ҡ��µ����ꡣ����������Ͻ�Ϊ����ԭ�㣬��λ��px���������ߴ��븴����һ�� 200��200 pixels �ľ���ѡ�������ѡ�����ڿ��Ա�������ճ����ԭͼ��	
'''
# crop, paste and merge
im = Image.open("E:/photoshop/lena.jpg")
box = (100,100,300,300)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)



'''
5������ͺϲ���ɫͨ��
���ڶ�ͨ��ͼ����ʱ���ڴ���ʱϣ���ܹ��ֱ��ÿ��ͨ������������ɺ����ºϳɶ�ͨ������Pillow�У��ܼ򵥣����£�
'''
r,g,b = im.split()
im = Image.merge("RGB", (r,g,b))


'''
 6�����α任
��ͼ����м��α任��һ�ֻ���������Pillow�а���resize( )��rotate( )�����÷����£�
���У�resize( )�����Ĳ�����һ����ͼ���С��Ԫ�棬��rotate( )����Ҫ����˳ʱ�����ת�Ƕȡ���Pillow�У�����һЩ��������ת����ר�ŵĶ��壺
'''
out = im.resize((128,128))
out = im.rotate(45)  # degree conter-clockwise
	
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)

'''
7����ɫ�ռ�任
�ڴ���ͼ��ʱ��������Ҫ������ɫ�ռ��ת�����罫��ɫת��Ϊ�Ҷȣ�
'''
cmyk = im.convert("CMYK")
gray = im.convert("L")
binary = im.convert("1")
rgb = im.convert("RGB")

'''
8��ͼ���˲�
ͼ���˲���ImageFilter ģ���У��ڸ�ģ���У�Ԥ�ȶ����˺ܶ���ǿ�˲���������ͨ��filter( )����ʹ�ã�Ԥ�����˲���������
BLUR��CONTOUR��DETAIL��EDGE_ENHANCE��EDGE_ENHANCE_MORE��EMBOSS��FIND_EDGES��SMOOTH��SMOOTH_MORE��SHARPEN������BLUR���Ǿ�ֵ�˲���CONTOUR��������FIND_EDGES��Ե��⣬ʹ�ø�ģ��ʱ�����ȵ��룬ʹ�÷������£�
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

