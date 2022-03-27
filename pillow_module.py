from PIL import Image,ImageFilter

before=Image.open('image 3.jpg')
#after=before.filter(ImageFilter.BoxBlur(10)) #BoxBlur is a command in-built in py to blurr imgs n 10 is the level of blurness
#after.save('resultant.jpg') #.save('theresult.extension') to save the result

after = before.filter(ImageFilter.FIND_EDGES())
after.save('result.jpg')
