from PIL import Image, ImageFilter
import os

image1 = Image.open('cat1.jpg')
image1.rotate(90).save('cat1_mod.jpg')
image1.convert(mode='L').save('cat1_L.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('cat1_filter.jpg')



# size_300 = (300, 300)
# size_700 = (700, 700)

# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
        
#         i.thumbnail(size_700)
#         i.save('700/{}_700.{}'.format(fn, fext))

#         i.thumbnail(size_300)
#         i.save('300/{}_300.{}'.format(fn, fext))



        # print(fext)

# image1 = Image.open('cat2.jpg')
# image1.save('cat1.png')
# image1.show()
