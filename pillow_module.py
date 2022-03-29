from PIL import Image,ImageFilter

before=Image.open("image 3.jpg")
after=before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")

before2=Image.open("image 3.jpg")
after2=before2.filter(ImageFilter.FIND_EDGES)
after.save("out2.bmp")