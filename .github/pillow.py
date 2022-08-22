from PIL import Image
from glob import glob
import os
p='D:\Download\images\*'
# Note: put this script in images folder
# Iterate through each file in the folder
for file in glob(p): # ignore hidden file (images/.DS_Store) from iteration
    image = Image.open(file).convert('RGB')
    # print(image.format, image.size, image.mode) # test
    
    path, filename = os.path.splitext(file)
    print(path)
     # get filename without extension
    image.rotate(270).resize((128,128)).save('{}.jpeg'.format(path))

print('OK')





from PIL import Image
from glob import glob
import os
home=os.path.expanduser('~')
path=home+'/image/*'


for file in glob('/home/student-04-62df7b1db086/images/*'):
    image = Image.open(file).convert('RGB')


    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))
