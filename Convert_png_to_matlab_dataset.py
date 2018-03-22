from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
import numpy as np
import scipy.io


def imageprepare(argv):

    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (20, 20), (255))  

    if width > height:  
       
        nheight = int(round((20.0 / width * height), 0))  
        if (nheight == 0): 
            nheight = 1
   
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((20 - nheight) / 2), 0)) 
        newImage.paste(img, (4, wtop)) 
    else:
        nwidth = int(round((20.0 / height * width), 0))  
        if (nwidth == 0): 
            nwidth = 1
    
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((20 - nwidth) / 2), 0))  
        newImage.paste(img, (wleft, 4)) 



    tv = list(newImage.getdata()) 
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    print(tva)
    return tva

x=[imageprepare('./3.png')]
print(len(x))
print(x[0])

newArr=[[0 for d in range(20)] for y in range(20)]
k = 0
for i in range(20):
    for j in range(20):
        newArr[i][j]=x[0][k]
        k=k+1

for i in range(20):
    for j in range(20):
        print(newArr[i][j])
    print('\n')

plt.imshow(newArr, interpolation='nearest')
newArr = np.asarray(newArr)
newArr = newArr.flatten('F')
scipy.io.savemat('own_created_dataset.mat',dict(X=newArr),y=3)
plt.show()
