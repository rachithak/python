import barcode
from barcode.writer import ImageWriter
text=input("enter text:")
code128=barcode.get_barcode_class('code128')
barcode_img=code128(text,writer=ImageWriter())
filename=barcode_image.save("my_barcode")
print("barcode saved:",filename)